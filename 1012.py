linha = input()
partes = linha.split()

pi = 3.14159
a = float(partes[0])
b = float(partes[1])
c = float(partes[2])

triangulo = a*c/2
circulo = pi*(c*c)
trapezio = c * ( a + b) / 2
quadrado = b*b
retangulo = a*b

print('TRIANGULO: %.3f'% triangulo)
print('CIRCULO: %.3f'% circulo)
print('TRAPEZIO: %.3f'% trapezio)
print('QUADRADO: %.3f'% quadrado)
print('RETANGULO: %.3f'% retangulo)


