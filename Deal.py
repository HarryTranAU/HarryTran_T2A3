class Deal:
    def __init__(self,
                 title: str,
                 link: str,
                 upvote: str,
                 downvote: str
                 ) -> None:
        self.title = title
        self.link = link
        self.upvote = upvote
        self.downvote = downvote

    def print_deal(self) -> None:
        print("Deal: " + self.title)
        print("Link: " + "https://www.ozbargain.com.au" + self.link)
        print("upvote: " + self.upvote)
        print("downvote: " + self.downvote)
