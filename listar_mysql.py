import mysql.connector

#=========Listar Tabelas e campos============
mydatabase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="detran"
)

mycursor = mydatabase.cursor()
mycursor.execute("SHOW TABLES")
myresultado = mycursor.fetchall()

for item in myresultado:
    print(item)
    mycursor.execute("SELECT * FROM {}".format(item[0]))
    myresultado = mycursor.fetchall()
    for item2 in myresultado:
        print(item2)


