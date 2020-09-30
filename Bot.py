from dhooks_lite import Webhook, Embed, Field
import re

# hook = Webhook(url)
# hook.execute('Hello, World!')


class Bot_discord:
    url = ""
    URL_REGEX = r'^(?:https?://)?((canary|ptb)\.)?discord(?:app)?\.com/api/' \
                r'webhooks/(?P<id>[0-9]+)/(?P<token>[A-Za-z0-9\.\-\_]+)/?$'

    @classmethod
    def set_url(cls, url):
        cls.url = url

    @classmethod
    def validate_url(cls, url):
        match = re.match(cls.URL_REGEX, url)
        if match is None:
            print("Invalid webhook URL provided. Go to README.md "
                  "for instructions on how to get your webhook correctly")
            return False
        else:
            return True

    @classmethod
    def send_deals(cls, deals):
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
