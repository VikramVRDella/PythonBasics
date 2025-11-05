from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI(
    
    title = "Sample FastAPI",
    description = "A Sample FastAPI Program",
    version="1.0.0"
)

@app.get("/home")
def home():
    return "You are at the Home Page..."
@app.get("/about")
def about():
    return "You are at the about page..."
@app.get("/services/{data}")
def services(data):
    return "You are at services of " +data
@app.get("/detail/{id}")
def detail(id:int):
    return f"data  {id}"

class cost(BaseModel):
    name:str
    price:int
@app.post("/cost")
def cost(co:cost):
    return co