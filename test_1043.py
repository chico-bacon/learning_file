a, b, c = input().split(' ')
a = float(a)
b = float(b)
c = float(c)
if (a > (b - c) and a < (b + c)) and (b > (a - c) and b < (a + c)) and (c > (a - b) and c < (a + b)):
    perimetro = a + b + c
    print('Perimetro = {}'.format(perimetro))
else:
    area = ((a + b)*c) / 2
    print('Area = {}'.format(area))
