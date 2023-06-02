n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
n3 = int(input("Digite o terceiro numero: "))

if n1 > n2 and n1>n3:
    print("O primeiro valor é o maior", n1)
elif n2 > n1 and n2 > n3:
    print("O segundo valor é o maior", n2)
else:
    print("O terceiro valor é o maior", n3)
