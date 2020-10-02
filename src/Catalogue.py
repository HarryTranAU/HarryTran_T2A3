from bs4 import BeautifulSoup
from Deal import Deal
from typing import List


class Catalogue:
    """ Class that represents a group of deals. """
    deals: List[Deal] = []

    def extract_deals(self, page: str) -> None:
        """ Turns a string object into the BeautifulSoup Data Structure """
        self.soup = BeautifulSoup(page, 'lxml')

    def populate_catalogue(self, threshold: int) -> None:
        """ Fills a list where each element is a Deal(class) """
        raw_deals = self.soup.find_all(class_="node-ozbdeal")
        self.deals = []
        print(f"\nUpvote Threshold: {threshold}\n")
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
        return self.deals
