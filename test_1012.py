def triangulo(height, base):
    area=(base*height)/2
    
    return area
def circulo(raio):
    pi=3.14159
    area=(pi*(raio**2))
    
    return area
    
def trapezio(base1, base2, height):
    area=((base1+base2)*height)/2
    
    return area
    
def quadradinde8(lado):
    area=B**2
    
    return area
    
def retangulo(base, height):
    area=base*height
    
    return area

A, B, C=input().split()
A=float(A)
B=float(B)
C=float(C)

print('TRIANGULO: {:.3f}'.format(triangulo(C, A)))
print('CIRCULO: {:.3f}'.format(circulo(C)))
print('TRAPEZIO: {:.3f}'.format(trapezio(A, B, C)))
print('QUADRADO: {:.3f}'.format(quadradinde8(B)))
print('RETANGULO: {:.3f}'.format(retangulo(A, B)))