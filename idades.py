#Função que cadastra pessoas recebendo nome e idade..
def cadastrar():
	nome, idade = input('Digite o nome e a idade: ').split(' ')
	peso = float(input('Digite o peso em kg: '))
	idade = int(idade)
	pessoa = {'nome': nome, 'idade': idade, 'peso': peso}
	
	return pessoa

#Função que exibe uma lista das pessoas cadastradas e suas respectivas idades...
def listar(lista):
	texto = ' LISTA '
	print('{:=^30}'.format(texto))
	for i in range(len(lista)):
			print('nome:{lista[i]["nome"]}, idade:{lista[i]["idade"]}anos , peso:{lista[i]["peso"]:.2f} kg')
	print('='*30)

#Função que soma todas as idades...
def somar(lista):
	soma = 0
	for i in range(len(lista)):
		soma += lista[i]["idade"]
	
	return soma

#Função que calcula a média de todas as idades...
def calcular_media():
	soma = somar(lista_pessoas)
	quantidade = len(lista_pessoas)
	media = soma / quantidade
	
	return media

#Função que procura e exibe a maior idade entre as pessoas cadastradas...
def achar_maior_idade(lista):
	maior_idade = lista[0]["idade"]
	for i in range(len(lista)):
		if lista[i]["idade"] > maior_idade:
			maior_idade = lista[i]["idade"]
	
	return maior_idade

def achar_pessoa_mais_velha(lista):
	maior_idade = achar_maior_idade(lista_pessoas)
	for i in range(len(lista)):
		if lista[i]["idade"] == maior_idade:
			print('A pessoa mais velha é:')
			print(f'Nome:{lista[i]["nome"]}    Idade:{lista[i]["idade"]}')
			break

def achar_mais_velhos(lista):
	maior_idade = achar_maior_idade(lista_pessoas)
	for i in range(len(lista)):
		if lista[i]["idade"] == maior_idade:
			print(f'Nome:{lista[i]["nome"]}    Idade:{lista[i]["idade"]}')
			
def somar_pesos(lista):
	soma = 0
	for i in range(len(lista)):
		soma += lista[i]["peso"]
	
	return soma
			
lista_pessoas = []
while True:
	print('[ 1 ] Cadastrar\n[ 2 ] Listar\n[ 3 ] Soma das idades\n[ 4 ] Médias das idades\n[ 5 ] Maior idade\n[ 6 ] Nome da pessoa mais velha\n[ 7 ] Nomes das pessoas mais velhas\n[ 8 ] Somar pesos\n[ 9 ] Sair\n')
	opcao = input('\nDigite sua opção: ')
	
	if opcao == '1':
		lista_pessoas.append(cadastrar())
	elif opcao == '2':
		listar(lista_pessoas)
		print('\n')
	elif opcao == '3':
		soma_idades = soma(lista_pessoas)
		print('\nA soma vale: {soma_idades}')
	elif opcao == '4':
		media = calcular_media()
		print(f'\nA media vale: {media:.1f}')
		print('\n')
	elif opcao == '5':
		print(f'A maior idade entre as pessoas cadastradas é {achar_maior_idade(lista_pessoas)}')
		print('\n')
	elif opcao == '6':
		achar_pessoa_mais_velha(lista_pessoas)
		print('\n')
	elif opcao == '7':
		achar_mais_velhos(lista_pessoas)
		print('\n')
	elif opcao == '8':
		soma_pesos = somar_pesos(lista_pessoas)
		print(f'Soma de todos os pesos vale: {soma_pesos} Kg')
	elif opcao == '9':
		break