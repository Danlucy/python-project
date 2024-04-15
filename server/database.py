# Datatype

import random 
import json

class Book:
    def __init__(self, title, subtitle, author, tag, publisher, ISBN, date):
        self.title = title
        self.subtitle = subtitle
        self.author = author
        self.tag = tag
        self.publisher = publisher
        self.ISBN = ISBN
        self.date = date

class User:
    def __init__(self, name, password, is_admin):
        self.name = name
        self.password = password
        self.is_admin = is_admin

# Database Object

class BookDatabase:
    def saveToFile(self):
        print("Saving book database to file")
        file_path = "data/book.json"

        book_list = []
        for book in self.books:
            book_list.append(book.__dict__)

        with open(file_path, "w") as json_file:
            json.dump(book_list, json_file, indent=4)

    def loadFromFile(self):
        print("Loading book database from file")
        
        self.books = []
        with open('data/book.json') as json_file:
            data = json.load(json_file)

        self.books = []
        for item in data:
            obj = Book(item['title'], item['subtitle'], item['author'], item['tag'], item['publisher'], item['ISBN'], item['date'])
            self.books.append(obj)

    def check(self):
        print(len(self.books))

class UserDatabase:
    def saveToFile(self):
        print("Saving user database to file")
        file_path = "data/user.json"

        objects_dict_list = []
        for user in self.users:
            user_list.append(user.__dict__)

        with open(file_path, "w") as json_file:
            json.dump(user_list, json_file, indent=4)

    def loadFromFile(self):
        print("Loading user database from file")
        
        self.users = []
        with open('data/user.json') as json_file:
            data = json.load(json_file)

        self.users = []
        for item in data:
            obj = User(item['name'], item['password'], item['is_admin'])
            self.users.append(obj)

    def check(self):
        print(len(self.users))

