lista = []

for c in range(0,5):
    n= int(input("Digite um numero: "))
    if c == 0 or n>lista[0]:
        lista.append(n)
    else:
        posicao = 0
        while posicao < len(lista):
            if n <= lista[posicao]:
                lista.insert(posicao,n)
                break
print (lista)
