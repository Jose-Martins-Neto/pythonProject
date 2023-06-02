i = 1
a = []
while i <= 5:
    numero = int(input("Insira um número: "))
    if numero %2 != 0:
        a.append(numero)
    i = i + 1
print(a)
