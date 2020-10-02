import requests

from Catalogue import Catalogue


class Ozbargain:
    """ Class representing the scraper function for specifically Ozbargain. """
    url = "https://www.ozbargain.com.au/"

    @classmethod
    def scrape(cls) -> str:
        cls.source = requests.get(cls.url).text
        return cls.source

    @staticmethod
    def frontpage(threshold) -> None:
        """ Function will scrape -> populate_catalogue -> print to terminal """
        ozb_catalog = Catalogue()
        ozb_catalog.extract_deals(Ozbargain.scrape())
        ozb_catalog.populate_catalogue(threshold)
        print("\n\n")
        if len(ozb_catalog.deals) == 0:
            print("No Deals meet the threshold. "
                  "Please lower the Upvote threshold in Options")
        for deal in ozb_catalog.deals:
            deal.print_deal()
            print("*************************\n")
