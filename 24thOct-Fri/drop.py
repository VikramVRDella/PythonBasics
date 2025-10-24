print(
    '''
    ***********************
    * DROP TABLE IN MYSQL *
    ***********************
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

sql="DROP TABLE IF EXISTS customers"
mycursor=mydb.cursor()
mycursor.execute(sql)