class Deal:
    def __init__(self, title, link, upvote, downvote):
        self.title = title
        self.link = "https://www.ozbargain.com.au" + link
        self.upvote = upvote
        self.downvote = downvote

    def printDeal(self):
        print(self.title)
        print(self.link)
        print(self.upvote)
        print(self.downvote)
