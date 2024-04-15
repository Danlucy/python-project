import json

class User:
    def __init__(self, name, password, is_admin):
        self.name = name
        self.password = password
        self.is_admin = is_admin

    def display(self):
        print(self.name)

class UserDatabase:
    def __init__(self):
        self.users = []

    def saveToFile(self):
        print("Saving user database to file")
        file_path = "user.json"

        objects_dict_list = []
        for user in self.users:
            user_list.append(user.__dict__)

        with open(file_path, "w") as json_file:
            json.dump(user_list, json_file, indent=4)

    def loadFromFile(self):
        print("Loading user database from file")
        
        with open('user.json') as json_file:
            data = json.load(json_file)

        self.users = []
        for item in data:
            obj = User(item['name'], item['password'], item['is_admin'])
            self.users.append(obj)

    def check(self):
        print(len(self.users))
