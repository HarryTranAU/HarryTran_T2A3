import unittest
from Bot import Bot_discord


class TestBot(unittest.TestCase):

    def test_validate_url(self):
        bot_cls = Bot_discord()
        bot_cls.url = "asdf"
        result = bot_cls.validate_url(bot_cls.url)
        self.assertFalse(result)
