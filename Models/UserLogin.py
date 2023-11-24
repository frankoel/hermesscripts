import json


class UserLogin:
    def __init__(self):
        self.email = "0123456789"
        self.password = True

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def from_json(self, json_received):
        self.email = json_received["email"]
        self.password = json_received["password"]


