import mysql.connector
import creditials as cd
mydb=mysql.connector.connect(
    host=cd.host,
    user=cd.user,
    password=cd.password
)

mycursor=mydb.cursor()

print(mydb)