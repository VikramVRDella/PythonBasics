print(
    '''
    ******************
    * Where in MYSQL *
    ******************
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
# sql="SELECT * FROM person ORDER BY name"  #Order by Ascending Order
sql="SELECT * FROM person ORDER BY name DESC" #Order by Desending Order
mycursor.execute(sql)
myresult=mycursor.fetchall()
for x in myresult:
    print(x)