from OZB_Scraper import OZB_Scraper
from Catalogue import Catalogue

ozb = OZB_Scraper("https://www.ozbargain.com.au/")

ozb_catalog = Catalogue()
ozb_catalog.extractDeals(ozb.scrape())
ozb_catalog.populateCatalogue()
for deal in ozb_catalog.deals:
    deal.printDeal()
    print("**********")
