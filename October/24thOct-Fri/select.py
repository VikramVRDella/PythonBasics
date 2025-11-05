print(
    '''
    *****************************
    * Select Commands for mysql *
    *****************************
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
mycursor.execute("SELECT * FROM person") #Selecting Full Table
# mycursor.execute("SELECT name FROM person") #Selecting Specific Row 
# myresult=mycursor.fetchall() # Fetching all Data
myresult=mycursor.fetchone() # Fetching One data
for x in myresult:
    print(x)