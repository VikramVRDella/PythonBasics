from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app=FastAPI()

class Create_product(BaseModel):
    name:str
    id:int
    desc:str

item=[]
@app.post("/create")
def create(cre:Create_product):
    item_collect={"name":cre.name,"id" : cre.id, "desc":cre.desc}
    item.append(item_collect)
    return 
@app.get("/view")
def view():
    return item

@app.get("/views/{pro_id}")
def single_view(pro_id:int):
    for i in item:
        if i["id"]==pro_id:
            return i["name"]
    return "Item not Found..."

@app.put("/update/{pid}")
def product(pid:int,pro:Create_product):
    for i in item:
        if i["id"] ==pid:
            i["name"]=pro.name
            i["id"]=pro.id
            i["desc"]=pro.desc
            return "Item is Updated..."
    raise HTTPException(status_code=404,detail="Item not Found...")
@app.delete("/delete/{pid}",status_code=201)
def dele(pid:int):
    for i in item:
        if i["id"]==pid:
            item.remove(i)
            return "Item Removed.."
    raise HTTPException(status_code=404,detail="Item not Found...")