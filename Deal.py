class Deal:
    def __init__(self, title, link, upvote, downvote):
        self.title = "Deal: " + title
        self.link = "Link: " + "https://www.ozbargain.com.au" + link
        self.upvote = "upvote: " + upvote
        self.downvote = "downvote: " + downvote

    def printDeal(self):
        print(self.title)
        print(self.link)
        print(self.upvote)
        print(self.downvote)
