lista = []

while True:
    lista.append (int(input("Digite um numero:")))
    resp = str(input("Deseja continuar? S/N: "))
    if resp in 'Nn':
        break
lista.sort()
print (lista)
