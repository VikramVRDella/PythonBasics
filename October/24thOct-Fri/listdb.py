print(
    '''
    ***********************
    * Python ShowDatabase * 
    ***********************
    '''
)

import mysql.connector
import creditials as cd

mydb=mysql.connector.connect(
    host=cd.host,
    user=cd.user,
    password=cd.password,
)

mycursor=mydb.cursor()
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)
