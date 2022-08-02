def cadastrar():
    print(f'{"cadastrando":=^20}')
    clientes = open("clientes.txt", "a")
    nome = input('Digite o nome: ')
    telefone = input('Digite o telefone: ')
    clientes.write(f'{nome:10}\t{telefone:10}\n')

def listar():
    print(f'{"listando":=^20}')
    print(f'{"nome":^10}\t{"telefone":^10}')
    clientes = open("clientes.txt", "r")
    lista = clientes.readlines()
    for cliente in lista:
        print(cliente)
    print('\n')

while True:
    print('1.cadastrar')
    print('2.listar')
    print('3.sair\n')
    opcao = int(input('Digite a opção desejada: '))
    if opcao == 1:
        cadastrar()
    elif opcao == 2:
        listar()
    else: 
        print('exit')
        break
