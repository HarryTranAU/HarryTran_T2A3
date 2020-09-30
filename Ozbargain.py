import requests
from Catalogue import Catalogue


class Ozbargain:
    url = "https://www.ozbargain.com.au/"

    @classmethod
    def scrape(cls):
        cls.source = requests.get(cls.url).text
        return cls.source

    @staticmethod
    def frontpage():
        ozb_catalog = Catalogue()
        ozb_catalog.extractDeals(Ozbargain.scrape())
        ozb_catalog.populateCatalogue()
        print("\n\n")
        if len(ozb_catalog.deals) == 0:
            print("No Deals meet the threshold. "
                  "Please lower the Upvote threshold in Options")
        for deal in ozb_catalog.deals:
            deal.printDeal()
            print("*************************\n")
