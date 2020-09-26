from Scraper import Scraper
from Catalogue import Catalogue

ozb = Scraper("https://www.ozbargain.com.au/")

ozb_catalog = Catalogue()
ozb_catalog.extractDeals(ozb.scrape())
ozb_catalog.populateCatalogue()
for deal in ozb_catalog.deals:
    deal.printDeal()
    print("**********")
