from typing import List
from fastapi import FastAPI
from models import User,Gender,Role
app=FastAPI()

db:List[User] =[
    User(
        id=1,
        name="John",
        age=21,
        gender=Gender.Male,
        roles=[Role.Admin]
    ),
    User(
        id=2,
        name="Doe",
        age=25,
        gender=Gender.Male,
        roles=[Role.Admin,Role.Teacher]
    ),
    User(
        id=3,
        name="Mary",
        age=23,
        gender=Gender.Female,
        roles=[Role.Teacher]
    )

]

@app.get("/")
async def get_hello():
    return {"Hello":"From FastAPI"}

@app.get("/api/db")
async def fetch_users():
    return db;
