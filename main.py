from bs4 import BeautifulSoup
import requests

source = requests.get("https://www.ozbargain.com.au/").text
soup = BeautifulSoup(source, 'lxml')

# Deal
deal = soup.find(class_="node-ozbdeal")

# Title
title = deal.find(class_="title").a.text
print(title)

# Link
link = deal.h2.a["href"]
print("https://www.ozbargain.com.au" + link)

# Upvote
upvote = deal.find(class_="nvb voteup").text
print(upvote)

# Downvote
downvote = deal.find(class_="nvb votedown").text
print(downvote)