print(
    '''
    ***************************************
    * Using Limit to Control the Function *
    ***************************************
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

# sql="SELECT * FROM person LIMIT 2"
sql="SELECT * FROM person LIMIT 2 OFFSET 0"
mycursor=mydb.cursor()
mycursor.execute(sql)
myresult=mycursor.fetchall()
for x in myresult:
    print(x)