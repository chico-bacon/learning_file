ent = input('Digite um valor binário: ')
bin = '0b'
value = bin+ent
int_value = int(value, 2)
value = value[2:]
print(value)

if int_value > 126:
	for i in range(0, len(value)):
		value = value[:len(value) - 1]
		print(value, end='  vale  ')
		int_value = int(value, 2)
		print(int_value)
		if int_value <= 126:
			break

'''
value = int(value, 2)
print(value)
'''