from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date
app=FastAPI(
    title="Age Calculator"
)

class BirthDay(BaseModel):
    year:int
    month:int
    day:int

@app.post("/age")
def age_calculator(data:BirthDay):
    today=date.today()
    dob=date(data.year,data.month,data.day)
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return {"age":age}