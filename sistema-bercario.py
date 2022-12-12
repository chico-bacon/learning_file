import mysql.connector

banco = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "rigby500",
    database = "bercario"
)

cursor = banco.cursor()

#FUNÇÕES DE COLETA DE DADOS!!!
def cadastrar(option):
    if option == 1:
        dados = {"nome":input("Nome: "),
                 "peso_nascimento":input('Peso: '),
                 "altura":input('Altura: '),
                 "id_mae":input('Mãe: '),
                 "id_medico":input('Medico: ')
                 }
        registrar_bebe(dados)

        return "Bebe cadastrado com sucesso!!!"

    elif option == 2:
        dados = {"nome":input("Nome: "),
                 "endereco":input("endereço: "),
                 "telefone":input("telefone: "),
                 "data_nascimento":input("Data de nascimento: ")
                 }
        registrar_mae(dados)

        return "Mãe cadastrada com sucesso!!!"

    elif option == 3:
        dados = {"crm":input("crm: "),
                 "nome":input("nome: "),
                 "telefone":input("telefone: "),
                 "especialidade":input("especialidade: ")
                 }
        registrar_medico(dados)

        return "Doutor(a) registrado com sucesso!!!"

    elif option == 4:
        dados = {"nome":input("especialidade: "),}
        registrar_especialidades(dados)

#FUNÇÕES DE INSERÇÃO DE DADOS...
def registrar_bebe(dict):
    sql = 'INSERT INTO bebes(nome, data_nascimento, peso_nascimento, altura, id_mae, id_medico) VALUES (%s, curdate(), %s, %s, %s, %s)'
    values = (dict["nome"], dict["peso_nascimento"], dict["altura"], dict["id_mae"], dict["id_medico"])
    cursor.execute(sql, values)
    banco.commit()

def registrar_mae(dict):
    sql = 'INSERT INTO maes(nome, endereco, telefone, data_nascimento) VALUES (%s, %s, %s, %s)'
    values = (dict["nome"], dict["endereco"], dict["telefone"], dict["data_nascimento"])
    cursor.execute(sql, values)
    banco.commit()

def registrar_medico(dict):
    sql = 'INSERT INTO medicos(crm, nome, telefone, id_especialidade) VALUES (%s, %s, %s, %s)'
    values = (dict["crm"], dict["nome"], dict["telefone"], dict["especialidade"])
    cursor.execute(sql, values)
    banco.commit()

def registrar_especialidades(dict):
    sql = 'INSERT INTO especialidades(nome) VALUES (%s)'
    values = (dict["nome"], )
    cursor.execute(sql, values)
    banco.commit()

#DEIXAR ESSA FUNÇÃO GENÉRICA PARA SER USADA EM TODAS AS TABELAS...
def consultar(sql1, sql2):
    cursor.execute(sql1)
    descricao = cursor.fetchall()
    cursor.execute(sql2)
    linhas= cursor.fetchall()

    for coluna in range(0, len(descricao)):
        print('{:^20}|'.format(descricao[coluna][0]),end='')
    print('\n',end='')
    print('-'*(len(descricao)*20))

    for linha in linhas:
        for dado in range(len(linha)-1):
            data = str(linha[len(linha)-1])
            print('{:^20}|'.format(linha[dado]),end='')
        print(data)
        print('\n')

    print('\n',end='')
    print('-'*(len(descricao)*20))
    print('\n')

def deletar(sql, value):
        cursor.execute(sql, value)
        banco.commit()

def atualizar(dados_atuais, colunas):

    id = int(input('Digite o id da mae que deseja alterar: '))

    result = list()
    for i in range(0, len(dados_atuais)):
        if id == dados_atuais[i][0]:
            result = dados_atuais[i]
    print(result)

    dados_novos = {"nome":input('Digite o nome: ').split(),
            "endereco":input('Digite o endereço: ').split(),
            "telefone":input('Digite o telefone: ').split(),
            "data_nascimento":input('Digite a data de nascimento(ano-mes-dia): ').split()
            }

    index = 1
    for i in dados_novos:
        if dados_novos[i] == '':
            dados_novos[i] = result[index]
        index+=1


while True:
    option = int(input('Digite 1 para inserir dados no banco\nDigite 2 para atualizar informações\nDigite 3 para consultar informações\nDigite 4 para deletar informações\nDigite 5 para sair\n'))

    if option == 1:
        print('[1] Bebe\n[2] Mae\n[3] Medico\n[4] Especialidade\n')
        opcao = int(input('Digite sua opção: '))
        cadastrar(opcao)

    elif option == 2:
        print('[1] Bebe\n[2] Mae\n[3] Medico\n[4] Especialidade\n')
        opcao = int(input('Digite sua opção: '))
        if opcao == 1:
            sql1 = 'SELECT * FROM bebes'
            sql2 = 'SHOW COLUMNS FROM bebes'
        elif opcao == 2:
             sql1 = 'SELECT * FROM maes'
             sql2 = 'SHOW COLUMNS FROM maes'
        elif opcao == 3:
             sql1 = 'SELECT * FROM medicos'
             sql2 = 'SHOW COLUMNS FROM medicos'
        elif opcao == 4:
             sql1 = 'SELECT * FROM especialidades'
             sql2 = 'SHOW COLUMNS FROM especialidades'
            
        cursor.execute(sql1)
        dados_atuais = cursor.fetchall()

        cursor.execute(sql2)
        dados = cursor.fetchall()
        colunas = list()
        for coluna in range(len(dados)):
            colunas.append(dados[coluna][0])

        atualizar()

    elif option == 3:
        print('[1] Bebe\n[2] Mae\n[3] Medico\n[4] Especialidade\n')
        opcao = int(input('Digite sua opção: '))
        if opcao == 1:
            sql1 = 'SHOW COLUMNS FROM bebes'
            sql2 = 'SELECT * FROM bebes'
            consultar(sql1,sql2)


        elif opcao == 2:
            sql1 = 'SHOW COLUMNS FROM maes'
            sql2 = 'SELECT * FROM maes'
            consultar(sql1,sql2)

        elif opcao == 3:
            sql1 = 'SHOW COLUMNS FROM medicos'
            sql2 = 'SELECT * FROM medicos'
            consultar(sql1,sql2)

        elif opcao == 4:
            sql1 = 'SHOW COLUMNS FROM especialidades'
            sql2 = 'SELECT * FROM especialidades'
            consultar(sql1,sql2)


    elif option == 4:
        print('[1] Bebe\n[2] Mae\n[3] Medico\n[4] Especialidade\n')
        opcao = int(input('Digite sua opção: '))
        if opcao == 1:
            sql = 'DELETE FROM bebes WHERE id=%s'
        elif opcao == 2:
            sql = 'DELETE FROM maes WHERE id=%s'
        elif opcao == 3:
            sql = 'DELETE FROM medicos WHERE id=%s'
        elif opcao == 4:
            sql = 'DELETE FROM especialidades WHERE id=%s'

        id = input("Digite o id da linha de informação que deseja apagar: ")
        value = (id,)
        deletar(sql,id)

    elif option == 5:
        break
    else:
        print('\033[31mOPÇÃO INVÁLIDA!!!\033[m\n')
        print('Tente novamente\n')
