from math import trunc

test_cases = int(input('Digite quantos casos de teste: '))

for h in range(0, test_cases):
	mensagem = list(input('Digite a mensagem {}: '.format(h + 1)))
	
	#passo 1: Primeira encriptação...
	for i in range(0, len(mensagem)):
		if mensagem[i] >= 'a' and mensagem[i] <= 'z' or mensagem[i] >= 'A' and mensagem[i] <= 'Z':
			codigo = ord(mensagem[i])
			codigo = codigo + 3
			codigo = chr(codigo)
			mensagem[i] = codigo
	
	#passo 2: Inversão da ordem da cifra...
	empty_list = list()
	for j in range((len(mensagem) - 1), -1, -1):
		empty_list += mensagem[j]
	mensagem = empty_list

	#passo 3: Reencriptação da metade da mensagem criptografada já obtida...
	pos = (trunc(len(mensagem)/2))
	for k in range(pos, len(mensagem)):
		cod = ord(mensagem[k])
		cod = cod - 1
		cod = chr(cod)
		mensagem[k] = cod
	mensagem = ''.join(mensagem)
	print(mensagem)
