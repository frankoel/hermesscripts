import json


class Company:
    def __init__(self):
        self.id = None
        self.name = "name"
        self.code = "0123456789"
        self.active = True

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def from_json(self, json_received):
        self.id = json_received["id"]
        self.name = json_received["name"]
        self.code = json_received["code"]
        self.active = float(json_received["active"])


