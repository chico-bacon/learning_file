while True:
    d, n = input().split(' ')
    if d == n == '0':
        break
    else:
        pass
    pos = n.find(d)
    wrong_number = n.replace(n[pos], "")
    wrong_number = int(wrong_number)
    print(wrong_number)