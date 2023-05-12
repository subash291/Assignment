from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient  # import mongo client to connect

# Creating instance of mongo client
client = MongoClient("mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23")


class Items(BaseModel):
    name: str
    description: str
    price: float


app = FastAPI()

inventory = []


@app.post("/add_items")
def create_item(item: Items):
    db = client.interns_b2_23
    item_instance = db.subhash
    item_instance.insert_one(item.dict())
    return {"message": "Items added successfully"}


@app.get("/getItemByName/{item_name}/")
def read_items():
    db = client.interns_b2_23
    item_instance = db.subhash
    item = item_instance.find({})
    item_details = []
    for items in item:
        item_detail = {'name': items['name'], 'description': items['description'], 'price': items['price']}
        item_details.append(item_detail)
    return {'item details': item_details}


@app.put("/item/{item_name}")
def update_items(item_name: str, item: Items):
    db = client.interns_b2_23
    item_instance = db.subhash
    condition = {"item_name": item_name}
    update = {"$set": {"name": item.name, "price": item.price}}
    item_instance.update_one(condition, update)
    return item

    # for index, existing_item in enumerate(inventory):
    #     db = client.interns_b2_23
    #     item_instance = db.subhash
    #     item_instance.update_one(item.dict())
    #     if existing_item.name == item_name:
    #         inventory[index] = item
    #         return {"message": "Items updated successfully"}
    #     return {"error": "Items not found"}


@app.delete("/deleteItemsByName/{item_name}")
def delete_item(item_name: str):
    db = client.interns_b2_23
    item_instance = db.subhash
    result = item_instance.delete_one({"name": item_name})
    if result.deleted_count > 0:
        return {"message": "Item deleted successfully"}
    else:
        return {"error": "Item not found"}
