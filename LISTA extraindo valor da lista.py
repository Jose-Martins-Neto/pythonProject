valores =[]
while True:
    valores.append(int(input("Digite um numero: ")))
    resposta = input("Deseja continuar? S/N : ")
    if resposta in 'Nn':
        break
print (valores)
if 5 in valores:
    print("O valor 5 faz parte da lista")
else:
    print("O valor 5 nao faz parte da lista!")