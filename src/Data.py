import json


class Data:
    """ Class handling saving and loading data from local storage """
    file_path = "config.json"
    threshold = 0

    def save(self, data: dict) -> None:
        with open(self.file_path, "w") as file_handler:
            json_string = json.dumps(data)
            file_handler.write(json_string)

    def load(self) -> dict:
        try:
            with open(self.file_path, "r") as file_handler:
                json_string = file_handler.read()
                return json.loads(json_string)
        except FileNotFoundError:
            return {"threshold": 0, "discord_hook": ""}
