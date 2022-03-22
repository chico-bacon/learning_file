from math import trunc

test_cases = int(input('Digite quantos casos de teste: '))

for h in range(0, test_cases):
    msg = str(input('Digite a mensagem {}: '.format(h + 1)))
    new_msg = str()

    #passo 1: Primeira encriptação...
    for i in range(0, len(msg)):
        cod = ord(msg[i])
        cod = cod + 3
        cod = chr(cod)
        new_msg += cod
    print(new_msg)

    #passo 2: Inversão da ordem da mensagem...
    letter = 0
    new_msg2 = str()
    for j in range((len(new_msg) - 1), -1, -1):
        new_msg2 += new_msg[j]
        letter += 1
    print(new_msg2)

    #passo 3: Reencriptação da metade da mensagem mensagem criptografada já obtida...
    pos = trunc(len(new_msg2)/2)
    new_msg3 = new_msg2[0:(pos-1)]
    for k in range(pos, len(new_msg2)):
        cod = ord(new_msg2[k])
        cod = cod - 1
        cod = chr(cod)
        new_msg3 += cod
    print(new_msg3)
