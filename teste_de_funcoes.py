import mysql.connector

banco = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "rigby500",
    database = "bercario"
)

cursor = banco.cursor()

sql1 = 'SELECT * FROM maes'
cursor.execute(sql1)
dados_atuais = cursor.fetchall()

sql2 = 'SHOW COLUMNS FROM maes'
cursor.execute(sql2)
dados = cursor.fetchall()
colunas = list()
for coluna in range(len(dados)):
    colunas.append(dados[coluna][0])

id = int(input('Digite o id da mae que deseja alterar: '))

result = list()
for i in range(0, len(dados_atuais)):
    if id == dados_atuais[i][0]:
        result = dados_atuais[i]
print(result)

dados_novos = dict()

index = 1
for i in dados_novos:
    if dados_novos[i] == '':
        dados_novos[i] = result[index]
    index+=1
print(dados)