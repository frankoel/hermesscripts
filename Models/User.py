import json


class User:
    def __init__(self):
        self.id = None
        self.name = "Fran"
        self.code = "0123456789"
        self.password = "0123456789"
        self.companyCode = "11112222A"
        self.active = True
        self.admin = True

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def from_json(self, json_received):
        self.id = json_received["id"]
        self.name = json_received["name"]
        self.code = json_received["code"]
        self.password = json_received["password"]        
        self.companyCode = json_received["companyCode"]
        self.active = float(json_received["active"])
        self.admin = float(json_received["admin"])


