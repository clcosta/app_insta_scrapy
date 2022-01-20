# Bem vindo ao **Portfolio APP Insta Scrapy**!
<p><img height="20" src="https://img.shields.io/badge/Version-BETA4.2-blue"/></p>

Este projeto ainda está em desenvolvimento, ele pretende pegar todas as publicações de um perfil no instagram e juntar todas as informações em uma unica aba dentro do google sheets para no futuro ser análisado todos os posts de um perfil e o seu crescimento ao longo do tempo.

## Redes Sociais
* [Instagram](https://www.instagram.com/claudiogfez/)
* [Linkedin](https://www.linkedin.com/in/clcostaf/)

# Pré requisitos

- Python 3.8 ou superior

- Selenium (instalação do driver não necessária)

- Google chrome

- Conta do google com uma permissão de ADM na plhanilha do google sheets


# Instalação

1. Primeiramente você pode clonar este repositório.

```
git clone https://github.com/clcosta/app_insta_scrapy.git
```

2. Agora a instalação das bibliotecas

*__OBS: Caso não encontre o terminal, pode digitar estas operações dentro do terminal do Pycharm__*

```
pip install -r requirements.txt
```

# Como utilizar

### __Configurações__
_Siga as instruções passo a passo!_ 

1. Primeiramnete é importantissimo você não utilizar sua conta no instagram para realizar a raspagem de dados de outro perfil, o instagram tem uma politica muito restrita contra qualquer perseguição e para sau conta não ser detectada como SPAM eu recomento criar uma outra conta só pra este proposito.<br><br>

2. Com a conta criada você terá de colocar o e-mail e senha no aplicativo na janela de configurações.<br><br>
 ![Configurações](https://i.ibb.co/F0RKvVB/usuario-senha.png)
<br><br>

3. Agora com o usuario e senha já colocados, precisamos colocar um ID de SESSÂO, que é basicamente um cookie gerado pelo instagram toda vez que você faz login no site.
 ![SESSION_ID](https://warehouse-camo.ingress.cmh1.psfhosted.org/53ef824d6e71053b3c1bf530da7004c04af479ee/68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f796f67657368776172616e30312f696e7374616772616d792f6d61737465722f73616d706c65732f73657373696f6e69642e676966)
<br><br>

4. Se você fez tudo correto até agora temos preenchidos os campos de usuario, senha e session id no aplicativo, agora só falta as informações do google sheets.
O id de uma plhanilha do google fica dentro do seu URL e ele pode ser encontrado sempre depois do *__/d/__* , como mostrado na imagem abaixo.<br><br>
![ID_SHEETS](https://i.ibb.co/KwDnMNR/image.png)

5. Agora você precisa de uma página de conexão dentro da sua planilha! Este é o mais simples, é so criar uma aba dentro do google sheets com o nome que desejar e escrever na célula A1 qualquer coisa, e depois colocar no ultimo campo o seguinte formato \<NOME DA PAGINA>!A1. No caso do exemplo abaixo ficaria *__Connection!A1__* <br><br>
![CONNECTION_RANGE](https://i.ibb.co/g4gLgzS/connection.png)
<br><br>

6. Por padrão desta aplicação a função de **Geral** já vem ativada, sendo assim é necessário criar também uma página dentro da planilha e chama-la de "Geral", escrito dessa forma obrigatoriamente.<br><br>
![GERAL](https://i.ibb.co/6wLrZ9X/geral.png)
<br><br>
### __Agora finalmente rodar o aplicativo__
  Com todas as configurações realizadas, recomendo reiniciar o aplicativo para ter certeza que todas ela foram aplicadas. Após o aplicativo reiniciar digite o nome de cada perfil separado em uma linha, exatamente como no exemplo abaixo, não utilize de virgulas ou espaços nem quaisquer caracter especial sómente o nome do usuario no instagram. O limitador funciona como uma limitador de posts que serão realizados o scraping, no exemplo a baixo está estabelecido um limite de 300 posts para cada perfil. Depois de clicar em raspar dados ele vai fazer o scraping da parte **Geral** do perfil primeiro e logo em seguida um google chrome automatizado será aberto e buscara a informação de todos os posts daquele perfil, com os links de todos os posts extraidos será realizado um scraping das informações mais detalhadas de cada post.<br><br>
![GERAL](https://i.ibb.co/gJBbxTt/limitador.png)
<br><br>

#### __CUIDADO!__
  Como foi falado, o aplicativo ainda está em desenvolvimento então não é recomendado utilizar para perfils com mais de 500 posts no limite, sendo que se for utilizar para varios perifls imagine que o limite para cada perfil diminui. Ou seja se for utilizar para 4 perfils com 500 posts você provavelmente terá um erro durante o 3 ou 4 perfil. As minhas recomendações são 2 a 3 perfils por vez sendo o "limite" mais baixo, _se passar de 500 posts por perfil o risco de um erro aumentará exponencialmente._

# Detalhes Técnicos
  O aplicativo funciona em 3 bases: 
  - Interface
  - Conexão 
  - Requisição

  _Não necessariamente nessa ordem_, onde cada uma delas tem seus detalhes e especificicações, vou explicar bem por cima de cada uma.

  ### __Interface__
  A criação da interface é feita utilizando a ferramenta PyQt5, Python e CSS são utilizados como base para montar a parte visual do app. Com a ferramenta, versões em .ui são criadas e os arquivos base estão disponibilizados nesse repositorio, na pasta __UI__ você pode ver os arquivos base da interface gráfica, onde o arquivo de imagem (file_rc_rc) está localizado na pasta __images__.

  ### __Conexão__
  A conexão com o google sheets é feita utilizando credenciais de Oauth que eu criei no meu google cloud, desta maneira são as credenciais de conexão que foi criado justamente para esse aplicativo, as credenciais são credenciais de teste então não é problema ser pública o arquivo está localizado na pasta __.\instascrapy\credentials.json__. Caso deseje criar suas proprias credenciais é so entrar neste [link](https://developers.google.com/workspace/guides/create-credentials).  
  Sendo a primeira execução do app, obrigatorio uma confirmação de conexão com o google sheets, já que você terá que dar permissão para editar as suas planilhas do google.
  ### __Requisição__
  O aplicativo utiliza a todo momento de requisições IO para o servidor do instagram.
  - primeira requisição: É feita durante a pesquisa do campo "geral", pegando informações de varios perfils ao mesmo tempo, a requisição geral utiliza de uma biblioteca externa que só tem este propósito.
  - segunda requisição: É feita com o objetivo de verificar se o perfil é privado ou público, já que os perfils que são privados não conseguimos ver os posts.
  - as proximas requisições: É feita durante o scraping dos detalhes dos posts, passando um parametro de url podemos obter um json de todas as informações básicas de um posts, durante a execução será criado uma pasta de cache, para cada perfil será criado um arquivo json, onde será feito a leitura dos detalhes do post neste arquivo. Até o momento atual as informações buscadas no pelo app são:
    - Data de postagem -> str
    - Link da publicação -> str
    - Número de Likes -> int
    - Número de Comentarios -> int
    - Número de visualizações do vídeo -> int
    - Se é video -> bool
    
# Autor
| [<img src="https://avatars.githubusercontent.com/u/83929403?v=4" width=120><br><sub>@clcostaf</sub>](https://github.com/clcosta) |
| :---: |
