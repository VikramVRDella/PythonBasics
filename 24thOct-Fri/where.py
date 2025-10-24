print(
    '''
    ****************************
    * Printing Where Statement *
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
# sql="SELECT * FROM person WHERE address ='Dubai Street'"
sql="SELECT * FROM person WHERE address LIKE '%Street%'"
mycursor.execute(sql)
myresult=mycursor.fetchall()
for x in myresult:
    print(x)