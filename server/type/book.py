import json
from faker import Faker

faker = Faker()
import random
import datetime

class Book:
    def __init__(self, title, subtitle, author, tag, publisher, ISBN, date):
        self.title = title
        self.subtitle = subtitle
        self.author = author
        self.tag = tag
        self.publisher = publisher
        self.ISBN = ISBN
        self.date = date

class BookDatabase:
    def __init__(self):
        self.books = [Book(faker.sentence(nb_words=3),faker.sentence(nb_words=10), faker.name(), [faker.sentence(nb_words=1) for _ in range(random.randint(0,5))], faker.name(), ''.join(str(random.randint(0, 9)) for _ in range(13)), datetime.date(random.randint(1900, 2022), random.randint(1, 12), random.randint(1, 28)).strftime("%Y-%m-%d %H:%M:%S")) for _ in range(1000)]


    def saveToFile(self):
        print("Saving book database to file")
        file_path = "book.json"

        book_list = []
        for book in self.books:
            book_list.append(book.__dict__)

        with open(file_path, "w") as json_file:
            json.dump(book_list, json_file, indent=4)

    def loadFromFile(self):
        print("Loading book database from file")
        
        with open('book.json') as json_file:
            data = json.load(json_file)

        self.books = []
        for item in data:
            obj = book(item['title'], item['subtitle'], item['author'], item['tag'], item['publisher'], item['ISBN'], item['date'])
            self.books.append(obj)

    def check(self):
        print(len(self.books))
