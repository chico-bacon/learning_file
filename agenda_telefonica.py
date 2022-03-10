lista_telefonica = []
lista_nome = []
while True:
    print('CADASTRAR - (1)\nLISTAR - (2)\nSAIR - (3)')
    opt = input('Digite a opção: ')

    if opt[0] == '1' or opt in 'cadastro':
        print('\nOpção 1 rodando...')
        text = 'CADASTRO'
        frm = len(text)+6
        print('='*frm)
        print('{:^3}'.format(text))
        print('='*frm)
        nome = str(input('Nome: '))
        number = str(input('Digite o numero de telefone: '))
        lista_telefonica.append(number)
        lista_nome.append(nome)
        print('\n')
    elif opt[0] == '2' or opt in 'listar':
        print('\nOpção 2 rodando')
        print('\n')
        text = 'LISTA TELEFONICA'
        frm = int(len(text)+6)
        print('='*frm)
        print('{:=^3}'.format(text))
        print('='*frm)
        for i in range(0, len(lista_telefonica)):
            print('pessoa {}: telefone: {}'.format(lista_nome[i], lista_telefonica[i]))
        print('='*frm)
        print('='*frm)
        print('\n')

    elif opt[0] == '3' or opt in 'sair':
        print('\nOpção 3 rodando')
        print('\nPrograma frinalizado')
        break
