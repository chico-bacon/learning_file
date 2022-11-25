import mysql.connector

database = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "",
    database = "detran"
)
#MOSTRAR TABELAS...
cursor = database.cursor()

cursor.execute("SHOW TABLES;")
tabelas = cursor.fetchall()
contador = 0
for item in tabelas:
    print(f'{item[0]}')

print('\n')

#VER VALORES...
while True:
    try:
        tabela = int(input("Digite a tabela que deseja consultar: "))
        sql1 = f"SELECT * FROM {tabelas[tabela][0]};"
        cursor.execute(sql1,)
        dados = cursor.fetchall()

    except:
        print('\033[31mOPÇÃO INVÁLIDA!!!\033[m')
    else:
        for linha in dados:
            print(linha)
        break

#DELETAR...
numero = int(input("Digite o indice da tabela que deseja alterar: "))
alvo = tabelas[numero][0]
valor = int(input("Digite o id do item que deseja apagar: "))
sql2 = f"DELETE FROM {alvo} WHERE id = {valor};"
cursor.execute(sql2,)
database.commit()

