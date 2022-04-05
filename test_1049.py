key_word1 = str(input())
key_word2 = str(input())
key_word3 = str(input())

if key_word1 == 'vertebrado':
	if key_word2 == 'ave':
		if key_word3 == 'carnivoro':
			print('aguia')
		elif key_word3 == 'onivoro':
			print('pomba')
	elif key_word2 == 'mamifero':
		if key_word3 == 'onivoro':
			print('homem')
		elif key_word3 == 'herbivoro':
			print('vaca')
elif key_word1 == 'invertebrado':
	if key_word2 == 'inseto':
		if key_word3 == 'hematofago':
			print('pulga')
		elif key_word3 == 'herbivoro':
			print('lagarta')
	elif key_word2 == 'anelideo':
		if key_word3 == 'hematofago':
			print('sanguessuga')
		elif key_word3 == 'onivoro':
			print('minhoca')
