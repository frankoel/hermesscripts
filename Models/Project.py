import json


class Project:
    def __init__(self):
        self.id = None
        self.name = "Proyecto Hermes"
        self.code = "111"
        self.codeCompany = "11112222A"
        self.description = "Descripcion del proyecto"
        self.active = True

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def from_json(self, json_received):
        self.id = json_received["id"]
        self.name = json_received["name"]
        self.code = json_received["code"]
        self.codeCompany = json_received["codeCompany"]
        self.description = json_received["description"]
        self.active = float(json_received["active"])


