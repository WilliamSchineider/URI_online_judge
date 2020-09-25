# Reads: Code of a product, number of units, price per unit

# Product 1
productCode1 = int(input())
unitsNumber1 = int(input())
pricePerUnit1 = float(input())

# Product 2
productCode2 = int(input())
unitsNumber2 = int(input())
pricePerUnit2 = float(input())

# Calculate the amount to be paid

totalValue = (unitsNumber1 * pricePerUnit1 + unitsNumber2 * pricePerUnit2)

# Output the total value

print('VALOR A PAGAR: R$', format(totalValue, '.2f'))