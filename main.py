"""import FastAPI"""
from fastapi import FastAPI

app = FastAPI()

""" perform simple arithmetic calculator"""


@app.post("/addition/'")
def addition(num1: float , num2: float):
    result = (num1+num2)
    return{"Addition of two number is": result}


@app.post("/subtraction/")
def subtraction(num1: float, num2: float):
    result= (num1-num2)
    return{"Subtraction of two number is": result}


@app.post("/multiplication/")
def multiplication(num1: float, num2: float):
    result = (num1*num2)
    return{"Multiplication of two number is": result}


@app.post("/division")
def division (num1: float, num2: float):
  try:
    result = (num1/num2)
    return{"division of two number is": result}
  except ZeroDivisionError:
    print("Error: Division by zero!")




