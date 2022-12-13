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

def atualizar(sql1, sql2, option):
        cursor.execute(sql1)
        resultado = cursor.fetchall()
        dados_atuais = list()
        for i in range(1, len(resultado[0])):
            dados_atuais.append(resultado[0][i])

        cursor.execute(sql2)
        resultado = cursor.fetchall()
        colunas = list()
        for j in range(len(resultado)):
            colunas.append(resultado[j][0])
        
        comando = 'UPDATE '

        if option == 1:
            tabela = 'bebes '
        elif option == 2:
            tabela = 'maes '
        elif option == 3:
            tabela = 'medicos '
        else:
            tabela = 'especialidades '
        sql = comando+tabela+'SET '

        linhas = list()
        for k in range(1, len(resultado)):
            linhas.append(resultado[k][0])
        print(linhas)
        print(dados_atuais)

        dados_novos = list()
        for m in range(len(linhas)):
            dados_novos.append(input(f'Digite {linhas[m]}: '))
            if dados_novos[m] == '':
                dados_novos[m] = dados_atuais[m]
        print(dados_novos)

        for l in range(len(linhas)):
            if dados_novos[l] in "datetime.date(":
                dados_novos[l] = 
            elif l < len(linhas)-1:
                sql = sql + linhas[l]
                sql = sql + '='
                sql = sql + dados_novos[l]
                sql = sql + ', '
            else:
                sql = sql + linhas[l]
                sql = sql + '='
                sql = sql + dados_novos[l]
                sql = sql + ' '
        sql = sql + 'WHERE id=' + id
        print(sql)
        




while True:
    option = int(input('Digite 1 para inserir dados no banco\nDigite 2 para atualizar informações\nDigite 3 para consultar informações\nDigite 4 para deletar informações\nDigite 5 para sair\n'))

    if option == 1:
        print('[1] Bebe\n[2] Mae\n[3] Medico\n[4] Especialidade\n')
        opcao = int(input('Digite sua opção: '))
        cadastrar(opcao)

    elif option == 2:
        print('[1] Bebe\n[2] Mae\n[3] Medico\n[4] Especialidade\n')
        opcao = int(input('Digite sua opção: '))
        id = input('Digite o id da tabela que deseja alterar: ')
        if opcao == 1:
            sql1 = 'SELECT * FROM bebes WHERE id='+id
            sql2 = 'SHOW COLUMNS FROM bebes'
        elif opcao == 2:
             sql1 = 'SELECT * FROM maes WHERE id='+id
             sql2 = 'SHOW COLUMNS FROM maes'
        elif opcao == 3:
             sql1 = 'SELECT * FROM medicos WHERE id='+id
             sql2 = 'SHOW COLUMNS FROM medicos'
        elif opcao == 4:
             sql1 = 'SELECT * FROM especialidades WHERE id='+id
             sql2 = 'SHOW COLUMNS FROM especialidades'
        
        atualizar(sql1, sql2, opcao)

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
