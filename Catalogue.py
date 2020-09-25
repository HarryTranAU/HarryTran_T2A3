from bs4 import BeautifulSoup
from Deal import Deal


class Catalogue:
    deals = []

    def extractDeals(self, page):
        self.soup = BeautifulSoup(page, 'lxml')

    def populateCatalogue(self):
        raw_deals = self.soup.find_all(class_="node-ozbdeal")
        for deal in raw_deals:
            title = deal.find(class_="title").a.text
            link = deal.h2.a["href"]
            upvote = deal.find(class_="nvb voteup").text
            downvote = deal.find(class_="nvb votedown").text

            temp_deal = Deal(title, link, upvote, downvote)
            self.deals.append(temp_deal)
