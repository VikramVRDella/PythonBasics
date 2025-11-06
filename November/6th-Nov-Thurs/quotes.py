from fastapi import FastAPI
import random

app=FastAPI(
    title="Quotes for Today"
)

quotes=[
    "Stay hungry, stay foolish.",
    "Code is like humor. When you have to explain it, it’s bad.",
    "Simplicity is the soul of efficiency.",
    "Make it work, make it right, make it fast."
]

@app.get("/quotes")
def today_quote():
    return {"Today's Quotes": random.choice(quotes)}