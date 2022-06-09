#coding: utf8
def cadastrar():
	dia, mes, ano = input('Digite a data (dia mês ano): ').split(' ')

	temperatura = float(input('Digite a temperatura em °C: '))

	dado = {'dia': dia, 'mes': mes, 'ano': ano, 'temperatura': temperatura}
	temperaturas.append(dado)

	return dado	

def listar(lista):
	print('\n')
	for item in lista:
		print(f'{item["dia"]}/{item["mes"]}/{item["ano"]} - {item["temperatura"]}°C')

def searchdate(dia, mes='0', ano='0'):
	print('\n')
	for i in range(0, len(temperaturas)):
		if mes == '0' and ano == '0':
			if temperaturas[i]['dia'] == dia:
				print(f'{temperaturas[i]["dia"]}/{temperaturas[i]["mes"]}/{temperaturas[i]["ano"]} - {temperaturas[i]["temperatura"]}°C')
			else:
				continue
				
def minimo(lista):
	

texto = '''		 [ 1 ] Cadastrar
		 [ 2 ] Listar
		 [ 3 ] Procurar por data
		 [ 4 ] Achar temperatura mínima
		 [ 5 ] Listar ordenado por temperatura
		 [ 6 ] Média das temperaturas
		 [ 7 ] Sair '''

temperaturas = []

while True:
	
	print('\n', texto)
	
	opcao = input('\nDigite sua opção: ')
	
	if opcao == '1':
		temperaturas.append(cadastrar())
	
	elif opcao == '2':
		listar(temperaturas)
		
	elif opcao == '3':
		dia = input('Digite o dia: ')
		searchdate(dia)