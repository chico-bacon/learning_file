'''
live_days = int(input())
month = 30
year = 365
dia = 0
mes = 0
ano = 0
while live_days > 0:
	if live_days >= year:
		live_days -= year
		ano += 1
	elif live_days >= month:
		live_days -= month
		mes += 1
	elif live_days < month:
		live_days -= 1
		dia += 1

print('{} ano(s)'.format(ano))
print('{} mes(es)'.format(mes))
print('{} dia(s)'.format(dia))
'''
live_days=int(input())
ano = live_days // 365
mes = int((live_days % 365) / 30)
dia = int((live_days % 365) % 30)
print('{} ano(s)'.format(ano))
print('{} mes(es)'.format(mes))
print('{} dia(s)'.format(dia))