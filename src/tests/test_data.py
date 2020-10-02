import unittest
import os
from Data import Data


class TestData(unittest.TestCase):

    def test_load(self):
        data_cls = Data()
        data_cls.file_path = "emptyFile.json"
        with open(data_cls.file_path, "w") as file_handler:
            file_handler.write("{}")
        rtn_value = data_cls.load()
        self.assertEqual(rtn_value, {})
        os.remove("emptyFile.json")

        rtn_value = data_cls.load()
        self.assertEqual(rtn_value, {"threshold": 0, "discord_hook": ""})
