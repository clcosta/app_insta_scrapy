# Bem vindo ao **Portfolio APP Insta Scrapy**!
<p><img height="20" src="https://img.shields.io/badge/Version-BETA4.0-blue"/></p>

Este projeto ainda está em desenvolvimento, ele pretende pegar todas as publicações de um perfil no instagram e juntar todas as informações em uma unica aba dentro do google sheets para no futuro ser análisado todos os posts de um perfil e o seu crescimento ao longo do tempo.

## Redes Sociais
* [Site](https://portfolio-claudio.herokuapp.com)
* [Instagram](https://www.instagram.com/claudiogfez/)
* [Linkedin](https://www.linkedin.com/in/clcostaf/)

# Pré requisitos

- Python 3.8 ou superior

- Selenium

- Google chrome

- Conta do google com uma permissão de ADM na plhanilha do google sheets


## Instalação

1. Primeiramente você pode clonar este repositório.

```
git clone https://github.com/clcosta/portfolio-django-flask.git
```

2. Agora a instalação das bibliotecas

*__OBS: Caso não encontre o terminal, pode digitar estas operações dentro do terminal do Pycharm__*

```
pip install -r requirements.txt
```

## Como utilizar

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

6. Por padrão desta aplicação a função de **Geral** já vem ativada, sendo assim é necessário criar também uma página dentro da planilha e chama-la de "Geral", escrito dessa forma obrigatoriamente.
<br><br>
### __Agora finalmente utilizar__
  Com todas as configurações realizadas, recomendo reiniciar o aplicativo para ter certeza que todas ela foram aplicadas, após o aplicativo reiniciar digite o nome de cada perfil separado em uma linha, não utilize de virgulas ou espaços nem qualquer caracter especial sómente o nome do usuario, depois de clicar em raspar dados ele vai fazer o scraping da parte **Geral** do perfil primeiro e logo em seguida abrira um google automatizado e buscara a informação de todos os posts daquele perfil.

#### __CUIDADO!__
  Como foi falado, o aplicativo ainda está em desenvolvimento então não é recomendado utilizar para perfils com mais de 500 posts, sendo que se for utilizar para varios perifls imagine que o limite para cada perfil diminui, ou seja se for utilizar para 4 perfils com 500 posts você provavelmente terá um erro durante o 3 ou 4 perfil, minhas recomendações são 2 a 3 perfils por vez sendo que eles não podem ter mais de 500 posts ou o risco de um erro aumentará exponencialmente.

# Autor
| [<img src="https://avatars.githubusercontent.com/u/83929403?v=4" width=120><br><sub>@clcostaf</sub>](https://github.com/clcosta) |
| :---: |
