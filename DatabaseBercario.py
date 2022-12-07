import mysql.connector

banco = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = '',
    database = "bercario"
)

cursor = banco.cursor()

def addbercario():
    print('[1] Cadastrar bebe\n[2] Cadastrar mãe\n[3] Cadastrar médico\n[4] Adicionar especilizações\n')
    option = input('Digite a sua opção: ')

def consulta():
    def searchmaes(option):
        if option == '1':
            sql = 'SELECT nome, endereco, telefone, data_nascimento as data de nascimento FROM maes'
            cursor.execute(sql)
        elif option == '2':
            sql = 'SELECT nome, endereco, telefone, data_nascimento as data de nascimento FROM maes WHERE nome=%s'

    print('[1] Nascimentos\n[2] Mães\n[3] Médicos\n[4]Nascidos\n')
    option = input('Digite a sua opção: ')

    if option == '1':
        sql = 'SELECT COUNT(%s) FROM bebes'
        numero = cursor.execute(sql)
        print('Foram registrados {} nascimentos nesse berçario.'.format(numero))
    
    elif option == '2':