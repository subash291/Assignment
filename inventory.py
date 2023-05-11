from fastapi import FastAPI
from pydantic import BaseModel


class Items(BaseModel):

    name: str
    description: str = None
    price: float


app = FastAPI()

inventory = []


@app.post("/add_items")
def create_item(item: Items):
     inventory.append(item)
     return {"message": "Items added successfully"}


@app.get("/getItemByName/{item_name}/")
def read_items(item_name: str):
    for items in inventory:
        if items.name == item_name:
            return items
        return {"error": "Items not found"}



@app.put("/item/{item_name}")
def update_items(item_name: str, item: Items):
    for index, existing_item in enumerate(inventory):
        if existing_item.name == item_name:
            inventory[index] = item
            return {"message": "Items updated successfully"}
        return {"error": "Items not found"}


@app.delete("/deleteItemsByName/{item_name}")
def delete_items(item_name: str):
    for index, item in enumerate(inventory):
        if item.name == item_name:
            inventory.pop(index)
            return {"message": "Items deleted successfully"}
    return {"error": "Items not found"}

