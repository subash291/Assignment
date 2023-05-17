from core.handlers.site_report_handler import delete_item, read_items, update_item, create_item, sending_item
from fastapi import APIRouter
from schemas.model import Items, Email

storage_router = APIRouter()


@storage_router.post("/add_items")
def goods(item: Items):
    return create_item(item)


@storage_router.get("/getItemByName/{item_name}/")
def goods(item_name=str):
    return read_items(item_name)


@storage_router.put("/item/{item_name}")
def goods(item_name: str, new_item: Items):
    return update_item(item_name, new_item)


@storage_router.delete("/deleteItemsByName/{item_name}")
def goods(item_name: str):
    return delete_item(item_name)


@storage_router.post("/send_email")
def feature(email: Email):
    return sending_item(email)
