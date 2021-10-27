import os

from .instagramscraping import InstagramScraping
from .instagramscrapingselenium import InstagramScrapingSelenium
from .sheets import GoogleSheets


class InstaScraping(InstagramScrapingSelenium, InstagramScraping, GoogleSheets):
    
    def __init__(self):
        InstagramScraping.__init__(self)
        InstagramScrapingSelenium.__init__(self)
        os.system('clear')
        GoogleSheets.__init__(self)
