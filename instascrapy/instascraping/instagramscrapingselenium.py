import json
import time
from datetime import datetime

import requests
from bs4 import BeautifulSoup
from instascrape.exceptions.exceptions import InstagramLoginRedirectError
from rich.console import Console
from rich.progress import track
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .auth import PASSWORD, SESSION_ID, USERNAME
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

class InstagramScrapingSelenium:
    """Está classe tem objetivo principal extrair a informação dos posts
    - Principal método get_posts(users: list, df: Optional[DataFrame])
    """
    console = Console()

    from webdriver_manager.chrome import ChromeDriverManager

    SLEEP_TIME = 5 # Start time sleep between scraping

    PASSWORD = PASSWORD

    USERNAME = USERNAME

    SESSION_ID = SESSION_ID

    def __init__(self, webdriver=ChromeDriverManager().install()):
        self.__webdriver = webdriver
        self.sleep_time = self.SLEEP_TIME

    def entrar_instagram(self):
        options = webdriver.ChromeOptions() 
        options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(self.__webdriver,options=options)
        self.driver.set_window_size(1024, 768)
        self.driver.get("https://www.instagram.com/")

    def fazer_login(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[3]/button'))) 
        self.driver.find_element_by_name('username').send_keys(f'{self.USERNAME}')
        self.driver.find_element_by_name('password').send_keys(f'{self.PASSWORD}')
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()

    def __pegar_SESSION_ID(self):
        all_cookies = self.driver.get_cookies()
        for i, j in enumerate(all_cookies):
            if all_cookies[i]['name'] == 'sessionid':
                self.SESSION_ID = j['value']
                return self.SESSION_ID

    def pular_primeiro_popup(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/section/div/button'))) 
        if element is None:
            return
        else:
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()

    def pular_segundo_popup(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@role="dialog"]'))) 
        if element is None:
            return None
        else:
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]'))) 
            self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()

    def esperar_post_carregar(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((
            By.XPATH,
            '//div[@class="v1Nh3 kIKUG  _bz0w"]/a'
            ))) 

    def pegar_n_posts(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.XPATH, '//span[@class="g47SY "]')))
        n_posts = self.driver.find_elements_by_xpath('//span[@class="g47SY "]')[0].text
        if '.' in n_posts: n_posts = n_posts.replace('.', '')
        if ',' in n_posts: n_posts = n_posts.replace(',', '')
        self.console.log(f'Foram encontrados [bold]{n_posts}[/] neste perfil!')
        return int(n_posts)

    def __tempo_de_espera_seguranca(self,time_s, multiplicador:int = 6):
        execucao = int(time_s*multiplicador)
        for t in track(range(execucao), f'Tempo até a extração do proximo perfil: {time_s*multiplicador} segundos'):
            time.sleep(1)



    def scraping_posts_infos(self, lista_de_perfils: list, sleep_time:int, between: int):

        if sleep_time is None: pass
        else: self.sleep_time = sleep_time

        self.console.log('Começando scraping dos detalhes dos posts')

        super_dict = {}
        for j, user in enumerate(lista_de_perfils):
            if j != 0 :
                self.console.log('Realizando tempo de espera por segurança!')
                self.__tempo_de_espera_seguranca(sleep_time)
            self.console.log(f'Iniciando extração do perfil [green]{user}[/]')
            self.driver.get(f'https://www.instagram.com/{user}')
            self.esperar_post_carregar()
            n = self.pegar_n_posts()
            posts = self.__scrapings_link_posts(n)
            data = {f'{user}': {}}
            likes_list = []
            comments_list = []
            is_video_list = []
            views_list = []
            date_list = []
            with self.console.status(f'[green]Realizando o scraping dos detalhes posts deste perfil!') as scraping:
                for i, post in enumerate(posts):
                    if i % between == 0 and i != 0:
                        self.console.log(f'Detalhes dos posts: {i}/{len(posts)}')
                        time.sleep(sleep_time)
                    likes, comments, is_video, views_count, date = self.scraping_posts_details(post=post,user=user)
                    if None in (likes, comments, is_video, views_count, date): return super_dict
                    likes_list.append(likes)
                    comments_list.append(comments)
                    is_video_list.append(is_video)
                    views_list.append(views_count)
                    date_list.append(date)
                    data.update({
                            f'{user}':{
                                'Data': date_list,
                                'Links': posts,
                                "Likes": likes_list,
                                "Comentarios": comments_list,
                                'Visualizações': views_list,
                                'Vídeo': is_video_list
                            }
                        }
                    )
            super_dict.update(data)
            self.console.log(f'Extração do perfil {user} realizada com [green]sucesso![/]')

        self.console.log('Scraping dos detalhes dos posts [green]Finalizado[/]')
        if super_dict is None: 
            if data != None: return data
        return super_dict

    def scraping_posts_details(self,
        post:str = None,
        user:str = None,
        headers: dict = {
                "Accept": "*/*",
                "User-Agent": "Thunder Client (https://www.thunderclient.io)",
                "cookie": f"sessionid={SESSION_ID};" 
            }
        ):
        def make_request(headers=None):
            if not headers:
                response = requests.get(post+'?__a=1')
            else:
                response = requests.get(post+'?__a=1', headers=headers)
            return response

        def make_headers():
            seession_id = self.__pegar_SESSION_ID()
            headers = {
                "Accept": "*/*",
                "User-Agent": "Thunder Client (https://www.thunderclient.io)",
                "cookie": f"sessionid={seession_id};" 
            }
            return headers

        response = make_request()
        
        if response.text == "":
            new_headers = make_headers()
            new_response = make_request(headers=new_headers)
            if not new_response.ok and new_response.text[0] not in ('<', '{'):
                new_response = make_request()
            else:
                response = new_response

        instascraping_cache = f'{BASE_DIR}\\.instascraping_cache'
        if not os.path.exists(instascraping_cache):os.mkdir(instascraping_cache) ### Create Cache dir

        with open(f'{instascraping_cache}/{user}.json', 'w') as resp:
            resp.write(response.text)

        with open(f'{instascraping_cache}/{user}.json', 'r') as resp:
            check = resp.readline(1)
            if check == '<':
                self.SESSION_ID = self.__pegar_SESSION_ID()
                headers = {
                    "Accept": "*/*",
                    "User-Agent": "Thunder Client (https://www.thunderclient.io)",
                    "cookie": f"sessionid={self.SESSION_ID};" 
                }
                response = make_request(headers)

                if response.text[0] != '{':
                    raise InstagramLoginRedirectError
            data = json.loads(response.text)

        post_data =  data['graphql']['shortcode_media']

        likes = post_data['edge_media_preview_like']['count']
        comments = post_data['edge_media_to_parent_comment']['count']
        is_video = post_data['is_video']
        if is_video == True:
            views_count = post_data['video_view_count']
        else:
            views_count = ''
        timestamp = post_data['taken_at_timestamp']
        date = datetime.fromtimestamp(timestamp)
        data_str = date.strftime('%d/%m/%Y')
        return likes, comments, is_video, views_count, data_str

    def get_posts(self, users: list, sleep_time=10, between=10):
        """
        Args
        ----------
            - users: [list] = Lista de usuarios do instagram necessário para pesquisar os posts.

            - sleep_time: Optional[int] = Argumento Opcional sobre o tempo de espera sobre o scraping de cada posts, necessário para evitar punições.

            - between: Optional[int] = Argumento Opcional sobre a de "quanto em quanto" o programa terá que realizar o sleep_time.

        Returns
        ----------
           Dict
        """
        try:
            self.entrar_instagram()
        except Exception as error:
            print("Error ao entrar no Instagram: ", error)
        try:
            self.fazer_login()
        except Exception as error:
            print("Error ao Fazer Login no Instagram: ", error)
        try:
            self.pular_primeiro_popup()
        except Exception as error:
            try: 
                element = self.driver.find_element_by_xpath('//p[@id="slfErrorAlert"]').get_attribute('innerHTML')
                if element == 'Aguarde alguns minutos antes de tentar novamente.': return print("Conta detectada como BOT")
            except Exception as error:
                self.console.log(f"Erro ao fazer login no Instagram: Conta detectada como BOT")
                raise error
        try:
            self.pular_segundo_popup()
        except Exception as error:
            self.console.log(f"Error ao Pular o segundo POPUP: {error}")
        try:
            d = self.scraping_posts_infos(users, sleep_time, between)
            self.console.log('Aplicação [green]Finalizada[/] com sucesso!')
            self.driver.quit()
            return d
        except InstagramLoginRedirectError as error:
            self.driver.quit()
            self.console.log('Instagram Login Redirect')
            raise error
        except Exception as error:
            self.driver.quit()
            self.console.log(f"Error ao pegar informação dos POSTs: {error}", )
            raise error


    def __scrapings_link_posts(self,n: int,max_failed_scroll=300) ->list:
        
        JS_SCROLL_SCRIPT = (
            "window.scrollTo(0, document.body.scrollHeight); var lenOfPage=document.body.scrollHeight; return lenOfPage;"
        )
        JS_PAGE_LENGTH_SCRIPT = (
            "var lenOfPage=document.body.scrollHeight; return lenOfPage;"
        )

        temp_posts = []
        scroll_attempts = 0
        last_position = self.driver.execute_script(JS_PAGE_LENGTH_SCRIPT)
        scrolling = True
        with self.console.status(f'[green]Realizando o scraping dos {n} link posts deste perfil!') as scraping:
            while scrolling:

                current_position = self.driver.execute_script(JS_SCROLL_SCRIPT)
                source_data = self.driver.page_source
                found_posts = self.__separate_posts(source_data)

                # Append found posts into total posts
                for post in found_posts:    
                    temp_posts.append(post)
                
                if current_position == last_position:
                    scroll_attempts += 1
                    if scroll_attempts > max_failed_scroll:
                        scrolling = False
                else:
                    scroll_attempts = 0
                    last_position = current_position

                p = set(temp_posts)
                if (len(p) == n) or (len(p) >= n):
                    break

            posts = list(p)
            self.console.log('Links extraidos com [bold]sucesso![/]')
            return posts

    def __separate_posts(self, source_data):
        post_soup = []

        soup = BeautifulSoup(source_data, features="lxml")
        anchor_tags = soup.find_all("a")
        post_tags = [tag for tag in anchor_tags if tag.find(
            "div", {"class": "eLAPa"})]

        #Filter new posts that have not been stored yet
        new_posts = [tag for tag in post_tags if tag not in post_soup]
        post_soup += new_posts
        
        return self.__create_post_objects(post_soup)

    def __create_post_objects(self, post_soup):
        posts = []
        for post in post_soup:
            url = post["href"]
            posts.append('https://www.instagram.com' + url)
        real_posts = set(posts)
        return real_posts