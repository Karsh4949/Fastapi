from fastapi import FastAPI
app = FastAPI()
@app.get("/add")
def add(number1: int, number2: int):
    return {"Addition:", number1 + number2}

@app.get("/sub")
def sub(number1: int, number2: int):  
    return {"Substraction:", number1-number2}

@app.get("/mul")
def mul(number1: int, number2: int):
    return {"Multiplication:", number1*number2}

@app.get("/div")
def div(number1: int, number2: int):
    return {"Division:", number1/number2}







    