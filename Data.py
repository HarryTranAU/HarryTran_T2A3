import json


class Data():
    file_path = "config.json"

    @classmethod
    def save(cls, data):
        with open(cls.file_path, "w") as file_handler:
            json_string = json.dumps(data)
            file_handler.write(json_string)

    @classmethod
    def load(cls):
        try:
            with open(cls.file_path, "r") as file_handler:
                json_string = file_handler.read()
                return json.loads(json_string)
        except FileNotFoundError:
            return {"threshold": 0, "discord_hook": ""}
