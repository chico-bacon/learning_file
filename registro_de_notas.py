#Funções para gerenciar a lista de alunos...
def cadastrar():
'''
	print('='*30)
	print('{:^20}'.format('REGISTRO DO ALUNO'))
	print('='*30)
	'''
	alunos.append(input('Digite o nome do aluno: '))
	notas.append(float(input('Digite a nota da prova 1: ')))
	notas.append(float(input('Digite a nota da prova 2: ')))
	'''
	print('\n')
	print('='*30)
'''
def listar():
	pos = 0
	'''
	print('='*20)
	print('{:^20}'.format('LISTA DE ALUNOS'))
	print('='*20)
	'''
	for i in range(len(alunos)):
		print('nome: ', alunos[i])
		print('notas: ', notas[pos],', ',notas[pos+1])
		pos += 2
		'''
	print('='*20)
	'''

#programa principal que irá usar das funções...
opcao = str()
alunos = []
notas = []
while opcao != '3':
'''
	print('='*25)
	print('{:^20}'.format('SCHOOLAR_REG'))
	print('='*25)
	'''
	print('[ 1 ] Cadastrar\n[ 2 ] Listar\n[ 3 ] Sair')
	opcao = input('Digite sua opção: ').strip()

	if opcao == '1':
		print('\n')
		cadastrar()
		print('\n')
	elif opcao == '2':
		print('\n')
		listar()
		print('\n')
	else:
		print('OPÇÃO INVÁLIDA!!!')
