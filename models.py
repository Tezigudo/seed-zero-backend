from pydantic import BaseModel
from typing import Union


class Item(BaseModel):
    name: str
    price: float

class Arithematics(BaseModel):
    first_number: float
    second_number: float
