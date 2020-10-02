import requests

from Catalogue import Catalogue


class Ozbargain:
    """ Class representing the scraper function for specifically Ozbargain. """
    url = "https://www.ozbargain.com.au/"
    source = requests.Response()

    @classmethod
    def scrape(cls) -> requests.Response:
        cls.source = requests.get(cls.url)
        return cls.source

    @staticmethod
    def frontpage(threshold) -> list:
        """ Function will scrape -> populate_catalogue -> print to terminal """
        ozb_catalog = Catalogue()
        ozb_response = Ozbargain.scrape()
        if ozb_response.status_code == 200:
            ozb_catalog.extract_deals(Ozbargain.scrape().text)
            current_deals = ozb_catalog.populate_catalogue(threshold)
            if len(current_deals) == 0:
                print("No Deals meet the threshold. "
                      "Please lower the Upvote threshold in Options")
            for deal in current_deals:
                deal.print_deal()
                print("*************************\n")
            return current_deals
        else:
            print(f"Status code {ozb_response.status_code}: "
                  "Website might be down. Please try again later")
            return []
