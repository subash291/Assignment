from pymongo import MongoClient  # import mongo client to connect

# Creating instance of mongo client
client = MongoClient("mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23")
db = client.interns_b2_23
item_instance = db.subhash