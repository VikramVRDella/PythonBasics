print(
    '''
    ******************************
    * UPDATE TABLES using Python *
    ******************************
    '''
)
import mysql.connector
import creditials as cd

mydb=mysql.connector.connect(
    host=cd.host,
    user=cd.user,
    password=cd.password,
    database=cd.database
)
mycursor=mydb.cursor()
sql="UPDATE person SET address = %s WHERE address = %s"
val=("Gandhi Street", "Nehru Street")
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount, "Row is Updated")