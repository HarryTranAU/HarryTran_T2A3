from dhooks_lite import Webhook, Embed, Field
import re


class BotDiscord:
    """
    A class used to encapsulate the interactions and functions related
    to a Discord Webhook
    """

    url = ""
    URL_REGEX = r'^(?:https?://)?((canary|ptb)\.)?discord(?:app)?\.com/api/' \
                r'webhooks/(?P<id>[0-9]+)/(?P<token>[A-Za-z0-9\.\-\_]+)/?$'

    @classmethod
    def set_url(cls, url: str) -> None:
        cls.url = url

    @classmethod
    def validate_url(cls, url: str) -> None:
        match = re.match(cls.URL_REGEX, url)
        if match is None:
            print("Invalid webhook URL provided. Go to README.md "
                  "for instructions on how to get your webhook correctly")
            return False
        else:
            return True

    @classmethod
    def send_deals(cls, deals: list) -> None:
        hook = Webhook(cls.url)
        for deal in deals:
            e1 = Embed(
                title=deal.title,
                url="https://www.ozbargain.com.au" + deal.link,
                color=0x5CDBF0,
                fields=[
                    Field('Upvote', deal.upvote),
                    Field('Downvote', deal.downvote)
                ]
            )
            hook.execute(
                "https://www.ozbargain.com.au" + deal.link,
                username="Ozbargain",
                embeds=[e1]
            )
