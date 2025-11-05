from fastapi import FastAPI

app=FastAPI()

@app.get("/books")
def books(limit:int):
    a=[
        {"101":"Python"},
        {"102":"Java"},
        {"103":"Javascript"},
        {"104":"Golang"}
    ]
    return f"Book is {a[:limit]}"