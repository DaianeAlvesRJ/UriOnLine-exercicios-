linha1 = input()
linha2 = input()
partes1 = linha1.split()
partes2 = linha2.split()

n1 = int(partes1[0])
n2 = int(partes1[1])
n3 = float(partes1[2])
n4 = int(partes2[0])
n5 = int(partes2[1])
n6 = float(partes2[2])



calc1 = n2*n3 
calc2 = n5*n6
total = calc1+calc2
print("VALOR A PAGAR: R$ %.2f"%total)