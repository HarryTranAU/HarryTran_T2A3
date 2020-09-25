import requests


class OZB_Scraper:
    def __init__(self, url):
        self.url = url

    def scrape(self):
        self.source = requests.get(self.url).text
        return self.source
