produto = float (input("Digite o valor do produto: "))

perc = (5/100)*produto
desc = produto-perc

print ("O produto que custava RS{}, com desconto passará a custar RS{}." .format(produto, desc))

