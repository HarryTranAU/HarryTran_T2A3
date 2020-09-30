from dhooks_lite import Webhook
import re

# url = "https://discordapp.com/api/webhooks/760471241525690439/"\
#       "RWdvFBYDYAX07mOsCSaoTV4hu_lC5XqEFhJry4zl1SU1mzeMn0DrG9-U9gL5KOF6WVrx"

# hook = Webhook(url)
# hook.execute('Hello, World!')


class Bot:
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
