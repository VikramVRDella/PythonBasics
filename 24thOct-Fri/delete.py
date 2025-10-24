print(
    '''
    **********************
    *  Delete in MYSQL   *
    **********************
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
sql="DELETE FROM person WHERE address = 'Gandhi Street'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "row is deleted")