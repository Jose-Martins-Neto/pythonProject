l1=[]
l2=[]
l3=[]

while True:
    num = int(input("Digite um numero: "))
    l1.append(num)

    if num %2 == 0:
        l2.append(num)
    else:
        l3.append(num)
    resp = input("Deseja continuar ? S/N: ")
    if resp in 'Nn':
        break


print (l1)
print (l2)
print (l3)