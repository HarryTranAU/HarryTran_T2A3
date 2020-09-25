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





# source = requests.get("https://www.ozbargain.com.au/").text
# soup = BeautifulSoup(source, 'lxml')

# # Deal
# deal = soup.find(class_="node-ozbdeal")

# # Title
# title = deal.find(class_="title").a.text
# print(title)

# # Link
# link = deal.h2.a["href"]
# print("https://www.ozbargain.com.au" + link)

# # Upvote
# upvote = deal.find(class_="nvb voteup").text
# print(upvote)

# # Downvote
# downvote = deal.find(class_="nvb votedown").text
# print(downvote)