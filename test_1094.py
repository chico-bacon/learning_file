testes = int(input())
total = ratos = sapos = coelhos = 0
for i in range(0, testes):
    quantidade, tipo = input().split(' ')
    quantidade = int(quantidade)
    tipo = tipo.upper()
    total += quantidade
    
    if tipo == 'R':
        ratos += quantidade
    elif tipo == 'S':
        sapos += quantidade
    elif tipo == 'C':
        coelhos += quantidade
        
    percentual_ratos = (ratos * 100) /total
    percentual_sapos = (sapos * 100) /total
    percentual_coelhos = (coelhos * 100) /total
    
print('Total: {} cobaias'.format(total))
print('Total de coelhos: {}'.format(coelhos))
print('Total de ratos: {}'.format(ratos))
print('Total de sapos: {}'.format(sapos))
print('Percentual de coelhos: {:.2f} %'.format(percentual_coelhos))
print('Percentual de ratos: {:.2f} %'.format(percentual_ratos))
print('Percentual de sapos: {:.2f} %'.format(percentual_sapos))
