from fastapi import FastAPI
import mysql.connector


app=FastAPI(
    title="Todo API"
)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="todo_db"
)

mycursor=mydb.cursor(dictionary=True)


@app.get("/")
def show_todo():
    mycursor.execute("SELECT * FROM TODO")
    rows = mycursor.fetchall()
    return {"result":rows}


@app.post("/task")
def add_todo(task:str):
    mycursor.execute(f"INSERT INTO TODO (task) VALUES ('{task}')")
    mydb.commit()
    return {"Task": task}

@app.put("/taskedit")
def edit_task(id:int,task:str):
    mycursor.execute(f"UPDATE TODO SET task= ('{task}') where id =('{id}')")
    mydb.commit()
    return {"Updated":task}

@app.delete("/deletetask")
def delete_task(id:int):
    mycursor.execute(f"DELETE FROM TODO WHERE id = ('{id}')")
    mydb.commit()
    return {"Deleted":id}