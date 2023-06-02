l1=[]
l2=[]
l3=[]
n = int(input("Quantos numeros vao ser usados?"))

while True:
    num = int(input("Digite um numero:"))
    l1.append(num)
    for x in range(1):
        if num %2 == 0:
            l2.append(num)
        elif num %2 != 0:
            l3.append(num)
    resp = (input("Deseja continuar? S/N : "))
    if resp in 'Nn':
        break

print(l1)
print(l2)
print(l3)