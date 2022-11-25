import mysql.connector

mydatabase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="detran"
    )

cursor = mydatabase.cursor()

sql = "SELECT nome FROM proprietarios WHERE nome LIKE %s;"
consulta = input("Digite o nome ou as letras iniciais do nome do proprietario:  ")+"%"
val = (consulta, )

cursor.execute(sql, val)
resultado = cursor.fetchall()
for item in resultado:
    print(resultado)