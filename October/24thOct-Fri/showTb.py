print(
    '''
    ****************************
    * Show Tables in Databases *
    ****************************
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

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)