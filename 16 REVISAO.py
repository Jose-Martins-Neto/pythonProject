inicio  = int(input("Digite a hora de inicio: "))
fim = int(input("Digite a hora do final: "))
horas = int
if inicio>fim:
    horas = (24-inicio)+fim
    print(horas)
else:
    print(fim-inicio)
