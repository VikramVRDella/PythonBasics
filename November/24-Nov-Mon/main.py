from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

origins=[
    "http://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def hello():
    return {"message":"Hello from Backend"}

@app.get("/hello")
def hello():
    return {"message":"Hello from FastAPI"}