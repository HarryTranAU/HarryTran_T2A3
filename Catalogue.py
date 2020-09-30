from bs4 import BeautifulSoup
from Deal import Deal


class Catalogue:
    deals = []

    def extractDeals(self, page: str) -> None:
        self.soup = BeautifulSoup(page, 'lxml')

    def populateCatalogue(self, threshold: int) -> None:
        raw_deals = self.soup.find_all(class_="node-ozbdeal")
        for deal in raw_deals:
            if deal.find(class_="expired"):
                continue
            elif int(deal.find(class_="nvb voteup").text) < threshold:
                continue
            title = deal.find(class_="title").a.text
            link = deal.h2.a["href"]
            upvote = deal.find(class_="nvb voteup").text
            downvote = deal.find(class_="nvb votedown").text

            temp_deal = Deal(title, link, upvote, downvote)
            self.deals.append(temp_deal)
