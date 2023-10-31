import json


class Dedication:
    def __init__(self):
        self.id = None
        self.hoursInit = "2023-08-25T09:00:00.0+02:00"
        self.hoursEnd = "2023-08-25T09:00:00.0+02:00"
        self.projectCode = "222"
        self.user = "75763090D"
        self.description = "La descripcion"

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def from_json(self, json_received):
        self.id = json_received["id"]
        self.hoursInit = json_received["hoursInit"]
        self.hoursEnd = json_received["hoursEnd"]
        self.projectCode = json_received["projectCode"]        
        self.user = json_received["user"]
        self.description = json_received["description"]


