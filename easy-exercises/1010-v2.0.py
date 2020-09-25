# Read product information in the same line: Code of a product, number of units, price per unit
# And transform into correct types

productCode1, unitsNumber1, pricePerUnit1 = input().split()
productCode1 = int(productCode1)
unitsNumber1 = int(unitsNumber1)
pricePerUnit1 = float(pricePerUnit1)

productCode2, unitsNumber2, pricePerUnit2 = input().split()
productCode2 = int(productCode2)
unitsNumber2 = int(unitsNumber2)
pricePerUnit2 = float(pricePerUnit2)

# Print the total value

totalValue = unitsNumber1 * pricePerUnit1 + unitsNumber2 * pricePerUnit2

print('VALOR A PAGAR: R$', format(totalValue, '.2f'))