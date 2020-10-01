import unittest
from Bot import BotDiscord


class TestBot(unittest.TestCase):

    def test_validate_url(self):
        bot_cls = BotDiscord()
        bot_cls.url = "asdf"
        result = bot_cls.validate_url(bot_cls.url)
        self.assertFalse(result)

        bot_cls = BotDiscord()
        bot_cls.url = "https://discordapp.com/api/webhooks/750471241525690439"\
                      "/RWdvFBYDYAX07mOsCSaoTV4hu_lC5XqEFhJry4zl1SU1mzeMn0DrG"\
                      "9-U9gL5KOF6WVrx"
        result = bot_cls.validate_url(bot_cls.url)
        self.assertTrue(result)

        bot_cls = BotDiscord()
        bot_cls.url = "[]"
        result = bot_cls.validate_url(bot_cls.url)
        self.assertFalse(result)

    def test_set_url(self):
        bot_cls = BotDiscord()
        self.assertEqual(bot_cls.url, "")
        real_url = "https://discordapp.com/api/webhooks/750471241525690439"\
                   "/RWdvFBYDYAX07mOsCSaoTV4hu_lC5XqEFhJry4zl1SU1mzeMn0DrG"\
                   "9-U9gL5KOF6WVrx"
        bot_cls.set_url(real_url)
        self.assertEqual(bot_cls.url, real_url)
