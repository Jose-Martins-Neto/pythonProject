import math
angulo = float (input("Digite o angulo: "))
seno = math.sin(math.radians(angulo))
print ("O angulo {} tem valor em seno de  {:.2f} " .format(angulo, seno))

cosseno = math.cos(math.radians(angulo))

print ("O angulo {} tem valor em consseno de {:.2f}" .format(angulo, cosseno))

tangente = math.tan(math.radians(angulo))

print ("O angulo {} tem valor em tangente de {:.2f}" .format(angulo, tangente))
