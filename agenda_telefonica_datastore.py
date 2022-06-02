from os import system

lista_telefonica = []
lista_nome = []

def cadastrar():
	contatos = open("dados.txt", "a")
	nome = str(input('Nome: '))
	number = str(input('Digite o numero de telefone: '))
	lista_telefonica.append(number)
	lista_nome.append(nome)
	contatos.write(f'nome : {nome}, telefone : {number}')
	contatos.write('\n')
	
def listar():
	contatos = open("dados.txt", "r")
	lista = contatos.readlines()
	for pessoa in lista:
		print(pessoa)

system('cls')	
while True:
	print('CADASTRAR - (1)\nLISTAR - (2)\nSAIR - (3)')
	opt = input('Digite a opção: ')

	if opt[0] == '1':
		system('cls')
		print('\nOpção 1 rodando...')
		text = 'CADASTRO'
		frm = len(text)+6
		print('='*frm)
		print('{:^3}'.format(text))
		print('='*frm)
		
		#Coletar dados do cliente...
		cadastrar()

	elif opt[0] == '2':
		print('\nOpção 2 rodando')
		print('\n')
		text = 'LISTA TELEFONICA'
		frm = int(len(text)+6)
		print('='*frm)
		print('{:=^3}'.format(text))
		print('='*frm)
		
		#Exibir os dados dos clientes...
		listar()

		print('='*frm)
		print('='*frm)
		print('\n')

	elif opt[0] == '3':
		system('cls')
		print('Fim do programa...')
		break
	else:
		system('cls')
		print('OPÇÃO INVÁLIDA!!!\n')
		print('Tente novamente...')
