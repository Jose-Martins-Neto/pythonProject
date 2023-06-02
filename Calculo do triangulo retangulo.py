'''co = float(input("Digite o valor do cateto oposto: "))
ca = float (input("Digite o valor do cateto adjacente: "))

h = co*co + ca*ca

h = h**0.5

print ("O valor da Hipotenusa é: {}" .format(h))'''

import math

#forma utilizando calculo da hipotenusa pela biblioteca 'math'

co = float(input("Digite o valor do cateto oposto: "))
ca = float(input("Digite o valor do cateto adjacente : "))

print ("O Valor da hipotenusa é:  {} " .format(math.hypot(co,ca)))


