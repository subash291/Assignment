from pydantic import BaseModel


class Items(BaseModel):
    name: str
    description: str
    price: float


class Email(BaseModel):
    rec_email: str
    subject: str
    body: str
