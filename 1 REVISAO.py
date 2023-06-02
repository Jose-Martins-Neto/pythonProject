n1 = int(input("Digite a primeira nota:"))
n2 = int(input("Digite a segunda  nota:"))

media = (n1+n2)/2

print(media)

if media >= 7:
    print("Aprovado")
elif media >=4:
    print("Recuperação")
else:
    print("Reprovado")