from pydantic import BaseModel

class Friend(BaseModel):
    name:str
    age:int
    year:int
f=Friend(name="John",age=32,year=2004)
print(f.dict())