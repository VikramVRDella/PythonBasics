from pydantic import BaseModel
from typing import Optional,List
from enum import Enum

class Gender(str,Enum):
    Male="male"
    Female="female"

class Role(str,Enum):
    Admin="admin"
    Teacher="teacher"
    Student="student"

class User(BaseModel):
    id:Optional[int]
    name:str
    age:int
    gender:Gender
    roles:List[Role]
