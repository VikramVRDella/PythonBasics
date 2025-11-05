from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
import mysql.connector
import creditials as cd

app=FastAPI()

mydb=mysql.connector.connect(
    host=cd.host,
    user=cd.user,
    password=cd.password,
    database=cd.database
)

mycursor=mydb.cursor()

class person(BaseModel):
    name:str
    age:int

@app.get("/viewuser")
def get_user(user_id:int=None):
    if user_id==None:
         mycursor.execute("SELECT * FROM PERSON")
         result=mycursor.fetchall()
         return {"person ": result}
    else:
        mycursor.execute(f"SELECT * FROM PERSON WHERE id ={user_id}")
        result=mycursor.fetchone()
        if not result:
            raise HTTPException(status_code=404,detail="User Not Found")
        else:
            return {"Person":result}

@app.post("/adduser")
def add_user(per:person):
    mycursor.execute(f"INSERT INTO PERSON (name,age) VALUES('{per.name}','{per.age}')")
    mydb.commit()
    return {"Person :", "User Created"}

@app.put("/updateuser")
def update_user(user_id:int,user:person):
    mycursor.execute(f"UPDATE PERSON SET name ='{user.name}' WHERE id ={user_id}")
    mydb.commit()
    return {"User": "Updated"}
@app.delete("/deleteuser")
def delete_user(user_id:int):
    mycursor.execute(f"DELETE FROM PERSON WHERE id = {user_id}")
    mydb.commit()
    return {"User":"Deleted"}
