print(
    '''
    *******************
    * Creating Tables *
    *******************
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

mycursor.execute("CREATE TABLE person (name VARCHAR(200), address VARCHAR(300))")
print("Table Created....")