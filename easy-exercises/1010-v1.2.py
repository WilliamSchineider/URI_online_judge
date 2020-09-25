# Read products information: Code of a product, number of units, price per unit

totalValue = []

count = 0
while count <= 1:
    productCode = input()
    unitsNumber = input()
    pricePerUnit = input()
    totalValue.append(int(unitsNumber) * float(pricePerUnit))
    count += 1

# Print the total value

totalValueOut = totalValue[0] + totalValue[1]

print('VALOR A PAGAR: R$', format(totalValueOut, '.2f'))