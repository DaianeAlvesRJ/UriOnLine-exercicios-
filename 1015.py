from math import sqrt

linha1 = input()
linha2 = input()

partes1=linha1.split()
partes2=linha2.split()

x1 = float(partes1[0])
y1 = float(partes1[1])
x2 = float(partes2[0])
y2 = float(partes2[1])

distancia = sqrt((x2-x1)**2 + (y2-y1)**2)
print('%.4f'%distancia)