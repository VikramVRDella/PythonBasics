from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def default():
    a= '''
    ***************************
    *  Enter your Choice :    *
    *  1.Addition (add)       *
    *  2.Subraction (sub)     *
    *  3.Multiplication (mul) *
    *  4.Division (div)       *
    *  5.Modulo (mod)         *
    ***************************
    '''
    return a

@app.get("/add")
def add(num1:int,num2:int):
    return f"Sum :{num1+num2}"
@app.get("/sub")
def sub(num1:int,num2:int):
    return f"Difference : {num1-num2}"
@app.get("/mul")
def mul(num1:int,num2:int):
    return f"Multiply :{num1*num2}"
@app.get("/div")
def div(num1:int,num2:int):
    return f"Division :{num1/num2}"
@app.get("/mod")
def mod(num1:int,num2:int):
    return f"Modulo :{num1%num2}"

