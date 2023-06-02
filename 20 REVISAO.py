num = []
impar = []
par = []
posit = []
negat = []
count = 0

for x in range(10):
    numeros = int(input("Digite um número: "))
    num.append(numeros)

for x in range(10):
    if num[x] % 2 == 0:
        par.append(num[x])
    else:
        impar.append(num[x])
    if num[x] >= 0:
        posit.append(num[x])
    else:
        negat.append(num[x])
    if num[x] == 0:
        count += 1

print(f"Ímpares: {impar} \nPares: {par} \nPositivos: {posit} \nNegativos: {negat} \nZeros: {count}")
