from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector
import creditials as cd

app = FastAPI()

class Person(BaseModel):
    name: str
    address: str
    id:int

def get_db_connection():
    return mysql.connector.connect(
        host=cd.host,
        user=cd.user,
        password=cd.password,
        database=cd.database
    )

@app.get("/viewsall")
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)  
    cursor.execute("SELECT * FROM person")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

@app.post("/createuser")
def create_user(pro: Person):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "INSERT INTO person (name, address) VALUES (%s, %s)"
    values = (pro.name, pro.address)
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "User Created Successfully"}
@app.put("/updateuser/{userid}")
def update_user(userid:int,pro:Person):
    conn=get_db_connection()
    cursor=conn.cursor() 
    cursor.execute(f"UPDATE person SET name= {pro.name} WHERE id={userid}")
    conn.commit()