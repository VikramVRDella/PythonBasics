from fastapi import FastAPI
from pydantic import BaseModel


def Calculate_BMI(weight:float,height:float):
    bmi=weight/(height**2)
    return bmi

def BMI_Category(bmi:float):
    if bmi <18.50:
        return "Underweight"
    elif bmi>18.50 and bmi<24.90:
        return "Normal"
    elif bmi>25.00 and bmi<29.90:
        return "Overweight"
    else:
        return "Obese"

app=FastAPI(
    title="BMI Calculator API"
)

@app.get("/bmi")
def BMI(wei:float,hei:float):
    bmi=Calculate_BMI(weight=wei,height=hei)
    category=BMI_Category(bmi)
    return{
        "Weight":wei,
        "Height":hei,
        "BMI Value":bmi,
        "Category":category
    }