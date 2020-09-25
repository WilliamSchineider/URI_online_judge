# Creat empty array for products information: Code of a product, number of units, price per unit

productInfo = []

# Receive input from user

count = 0
while count <= 5:
    userInput = input()
    productInfo.append(userInput)
    count += 1

# Output the total value

totalValue = int(productInfo[1]) * float(productInfo[2]) + int(productInfo[4]) * float(productInfo[5])

print('VALOR A PAGAR: R$', format(totalValue, '.2f'))