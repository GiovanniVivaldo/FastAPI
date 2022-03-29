from pymongo import MongoClient

mongo_url = 'mongodb+srv://GiovanniVivaldo:fdWWmvqFsNjPXujP@cluster0.j3qff.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'

conn = MongoClient(mongo_url)