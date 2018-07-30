import json, os, uuid


class User:

    def __init__(self):
        self.isim = ""
        self.soyisim = ""
        self.numara = ""


class DBMethods:

    def __init__(self):
        self.path = "database.json"
        self.Create_db_if_not_exists()

    def Create_db_if_not_exists(self):
        if not os.path.exists(self.path):
            with open(self.path, "w") as f:
                json.dump({}, f)

    def add(self, user):
        with open(self.path, "r") as f:
            js = json.load(f)

        js.update({
            str(uuid.uuid1()): user.__dict__
        })
        with open(self.path, "w") as f:
            json.dump(js, f)

    def update(self, user, user_id):
        with open(self.path, "r") as f:
            js = json.load(f)

        if user_id in js:
            js[user_id] = user.__dict__

        with open(self.path, "w") as f:
            json.dump(js, f)

    def get(self):
        with open(self.path) as f:
            js = json.load(f)
        return js

    def delete(self, user_id):
        result = False
        with open(self.path, "r") as f:
            js = json.load(f)
        if user_id in js.keys():
            del js[user_id]
            result = True

        with open(self.path, "w") as f:
            json.dump(js, f)
        return result

    def Check_UserID(self, user_id):
        with open(self.path, "r") as f:
            js = json.load(f)

        return user_id in js
