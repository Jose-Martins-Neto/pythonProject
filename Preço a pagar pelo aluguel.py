km = float(input("Quantos quilometros rodados?"))
dias = int(input("Quantos dias o carro foi utilizado?"))

vd = 60*dias
vkm = 0.15*km

print ("O valor total a ser pago é: ", (vkm+vd))
