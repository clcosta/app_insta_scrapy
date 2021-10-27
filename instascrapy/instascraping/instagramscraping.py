import json
import time

import requests
from instagramy import InstagramUser
from rich.console import Console

from .auth import SESSION_ID


class InstagramScraping:
    """Está classe tem o objetivo principal de pegar informações dos perfils fornecidos atraves de uma lista ou de um unico perfil
    """

    console = Console()

    SLEEP_TIME = 10

    def __scraping_list_users_infos(self, usernames: list, sleep_time):

        if sleep_time is None: pass
        else: self.sleep_time = sleep_time

        followers = []
        following = []
        posts = []
        for i, username in enumerate(usernames):
            i+=1
            if i % 10 == 0 and i != 0:
                self.console.log(f'Extraindo detalhes dos perfils: {i}/{len(usernames)}')
                time.sleep(self.sleep_time)

            user = InstagramUser(username)
            followers.append(user.number_of_followers)
            following.append(user.number_of_followings)
            posts.append(user.number_of_posts)
        self.console.log(f'Extraido detalhes de {i} perfils')
        data = {
            "Usernames": usernames,
            "Followers": followers,
            "Following": following,
            "Posts": posts,
        }
        return data
    
    def __alternative_scraping_list_users_infos(self,usernames: list, sleep_time):
        
        if sleep_time is None: pass
        else: self.sleep_time = sleep_time
        
        followers = []
        following = []
        posts = []
        
        for user in usernames:
            
            headers = {
                "Accept": "*/*",
                "User-Agent": "Thunder Client (https://www.thunderclient.io)",
                "cookie": f"sessionid={SESSION_ID};" 
            }

            link  = f'https://www.instagram.com/{user}/?__a=1'

            response = requests.get(link, headers=headers)

            if response.ok and response.text[0] == '{':
                data = json.loads(response.text)

                number_of_posts = data['graphql']['user']['edge_owner_to_timeline_media']['count']
                number_of_followers = data['graphql']['user']['edge_followed_by']['count']
                number_of_followings = data['graphql']['user']['edge_follow']['count']

            else:
                raise 'SESSION ID ERRORs'

            followers.append(number_of_followers)
            following.append(number_of_followings)
            posts.append(number_of_posts)
        self.console.log(f'Extraido detalhes de {len(usernames)} perfils')
        data = {
            "Usernames": usernames,
            "Followers": followers,
            "Following": following,
            "Posts": posts,
        }
        return data
        

    def get_users_follows_infos(self, users: list, sleep_time: int = None) -> dict:
        """Pega uma lista de perfils e extrai as principais informações de número de seguidores
        quantidade de pessoas que segue, e número de posts.

        Args
        ----------
            users (list): username de cada perfil

        Raises
        ----------
            TypeError: attribute 'Users' need to be a list of usernames

        Returns
        ----------
            Dict: -> {Usernames: list[str], Followers: list[int], Following: list[int], Posts: list[int]}
        """
        try:
            for i, user in enumerate(users):
                if ' ' in user:
                    user = user.replace(' ', '')
                users[i] = user.lower()
            if type(users) == list:
                try:
                    df = self.__scraping_list_users_infos(users, sleep_time)
                except:
                    self.console.log('Erro ao pegar info de varios perfils, tentando novamente')
                    df = self.__alternative_scraping_list_users_infos(users, sleep_time)
                return df
            elif type(users) != list:
                raise TypeError("Parameter 'users' need to be a list type")
        except Exception as error:
            print("Error ao Pegar informação de varios perfils: ", error)
