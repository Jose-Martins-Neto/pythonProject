validos = int(input("Digite o numero de votos validos: "))
brancos = int(input("Digite o numero de votos em branco: "))
nulos = int(input("Digite o numero de votos nulos: "))

eleitores = brancos+validos+nulos

valido = validos/eleitores*100

branco = brancos/eleitores*100

nulo = nulos/eleitores*100

print(valido)
print(branco)
print(nulo)
