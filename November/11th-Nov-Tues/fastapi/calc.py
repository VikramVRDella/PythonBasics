from fastapi import FastAPI

app=FastAPI()

@app.get('/')
def calculator(choice,a:int,b:int):
    # choice=input("Enter your Choice : ")

    match choice:
        case "add":
            c=a+b
            return {"Sum":c}
        case "sub":
            c=a-b
            return {"Subract":c}
        case "mul":
            c=a*b
            return {"Multiply":c}
        case "div":
            a=float(a)
            b=float(b)
            c=a/b
            return {"Division":c}
