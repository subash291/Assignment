from core.handlers.email_handler import Email_handler, send_email
from schemas.model import Items, Email
from utility.mongo_utlity import item_instance


def create_item(item: Items):
    item_instance.insert_one(item.dict())
    return {"message": "Items added successfully"}


def read_items(item_name=str):
    try:
        item = item_instance.find_one({"name": item_name})
        if item:
            return {"message": "item is available"}
        return {"error occur": "item is not available"}
    except Exception as e:
        return{"error": str(e)}


# def update_items(item_name: str, item: Items):
#     condition = {"item_name": item_name}
#     update = {"$set": {"name": item.name, "price": item.price}}
#     item_instance.update_one(condition, update)
#     return item

    # for index, existing_item in enumerate(inventory):
    #     db = client.interns_b2_23
    #     item_instance = db.subhash
    #     item_instance.update_one(item.dict())
    #     if existing_item.name == item_name:
    #         inventory[index] = item
    #         return {"message": "Items updated successfully"}
    #     return {"error": "Items not found"}


def update_item(item_name: str, new_item: Items):
    try:
        result = item_instance.update_one({"name": item_name}, {"$set": new_item.__dict__})
        if result.modified_count > 0:
            return {"message": "item added successfully"}
        return {"error": "item not found"}
    except Exception as e:
        return {"error": str(e)}





def delete_item(item_name: str):
    result = item_instance.delete_one({"name": item_name})
    if result.deleted_count > 0:
        return {"message": "Item deleted successfully"}
    else:
        return {"error": "Item not found"}


def sending_item(email: Email):
    item_object = Email_handler()
    send_items = send_email(email)
    return {"Email sent successfully"}


