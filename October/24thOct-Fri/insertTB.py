print(
    '''
    **************************
    * Python Insert Database *
    **************************
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

# sql="INSERT INTO person (name,address) VALUES('John','Dubai Street')"
# sql="INSERT INTO PERSON (name,address) VALUES(%s,%s)"
# val=[
#     ('Peter', 'Dubai Main Road'),
#     ('Glora', 'African Street')
# ]
# mycursor.executemany(sql,val)
# mydb.commit()
# print("Inserted Value.....")
print(
    '''
    **********************
    * Insert ID Printing *
    **********************
    '''
)
sql="INSERT INTO person (name,address) VALUES(%s,%s)"
val=("Michel","Gandhi Street")
mycursor.execute(sql,val)
mydb.commit()
print("1 row Inserted , ID : ",mycursor.lastrowid)