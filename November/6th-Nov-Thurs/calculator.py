from fastapi import FastAPI

app=FastAPI(
     title="Calculator API"
)

@app.get("/calculator")
def Calculator(operation:str,b:int,c:int):
     if operation=="add":
          return b+c
     elif operation=="sub":
          return b-c
     elif operation=="mul":
          return b*c
     elif operation=="div":
          return b/c
     elif operation=="mod":
          return b%c
