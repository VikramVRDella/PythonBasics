from fastapi import FastAPI
# from pydantic import BaseModel

app=FastAPI(
    title="C 2 F and F 2 C"
)

@app.get("/farenheitConversion")
def celcius_to_farenheit(celcius:float):
    result = (celcius*(9/5)+32)
    rounded=round(result,2)
    return {"Farenheit" :f"{rounded} F"}
@app.get("/celciusConversion")
def farenheit_to_celcius(farenheit:float):
    result= (farenheit-32)*(5/9)
    rounded=round(result,2)
    return {"Celcius":f"{rounded} C"}