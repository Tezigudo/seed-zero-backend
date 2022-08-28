from models import Item, Arithematics
from http.client import HTTPException
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
import os
load_dotenv()


NAME = os.getenv('NAME', default="World")

app = FastAPI()


@app.get("/")
def index():
    return {"message": f"Hello {NAME}"}


@app.get("/calculator/add/")
def adder(num: Arithematics):
    return {"first_number": num.first_number, "second_number": num.second_number, "result": num.first_number+num.second_number}


@app.get("/calculator/substract")
def subtractor(num: Arithematics):
    return {"first_number": num.first_number, "second_number": num.second_number, "result": num.first_number-num.second_number}


@app.get("/calculator/multiply")
def multiply(num: Arithematics):
    return {"first_number": num.first_number, "second_number": num.second_number, "result": num.first_number*num.second_number}


@app.get("/calculator/divide")
def divide(num: Arithematics):
    return {"first_number": num.first_number, "second_number": num.second_number, "result": num.first_number/num.second_number}


@app.get("/{userId}")
def usersInfo(userId: int):
    if userId != 9997:
        raise HTTPException(status_code=404, detail="UserId not found.")

    return {
        "id": userId,
        "name": "Safe",
        "surname": "suk",
    }


# Example Request Body:
# {
#   "name": "Book",
#   "price": 123,
# }
@app.post("/item/create/")
def itemCreator(item: Item):
    print(item.name, item.price)
    return item.name, item.price
