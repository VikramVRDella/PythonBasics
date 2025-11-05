print(
    '''
    *******************
    * Python AlterSQL *
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

mycursor.execute("ALTER TABLE person ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
print("Table Altered.....")