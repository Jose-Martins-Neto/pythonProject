lista = []
maior = 0
menor = 0

for v in range (0,3):
    lista.append( int(input("Digite um numero: ")))
    if v == 0:
        maior = menor = lista[v]
    else:
        if lista[v] > maior:
            maior = lista[v]
        if lista[v] < menor:
            menor = lista[v]
print (maior)
print (menor)
print (lista)