from fastapi import FastAPI

app=FastAPI()

@app.get("/default")
def default():
    return "Hello Friend!!!"
@app.get("/{name}")
def person(name):
    return f"Hello {name}!!!"