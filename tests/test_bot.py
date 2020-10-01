import unittest
from Bot import BotDiscord


class TestBot(unittest.TestCase):

    def test_validate_url(self):
        bot_cls = BotDiscord()
        bot_cls.url = "asdf"
        result = bot_cls.validate_url(bot_cls.url)
        self.assertFalse(result)
