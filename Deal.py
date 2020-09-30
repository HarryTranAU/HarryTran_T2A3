class Deal:
    def __init__(self, title, link, upvote, downvote):
        self.title = title
        self.link = link
        self.upvote = upvote
        self.downvote = downvote

    def printDeal(self):
        print("Deal: " + self.title)
        print("Link: " + "https://www.ozbargain.com.au" + self.link)
        print("upvote: " + self.upvote)
        print("downvote: " + self.downvote)
