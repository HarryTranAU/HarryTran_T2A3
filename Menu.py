from Scraper import Scraper
from Catalogue import Catalogue


class Menu:
    @staticmethod
    def menu_options():
        menu_choice = input("""Welcome! Please input a number option below:
        1. Frontpage Deals
        9. Exit
        Input: """)
        return menu_choice

    @staticmethod
    def frontpage():
        ozb = Scraper("https://www.ozbargain.com.au/")

        ozb_catalog = Catalogue()
        ozb_catalog.extractDeals(ozb.scrape())
        ozb_catalog.populateCatalogue()
        for deal in ozb_catalog.deals:
            deal.printDeal()
            print("**********")
