# Create empty array

numberArray = []

# Reads input from user

firstNumber = int(input())
secondNumber = int(input())
thirdNumber = int(input())
fourthNumber = int(input())
fifthNumber = int(input())

# Include numbers in the empty array

numberArray.append(firstNumber)
numberArray.append(secondNumber)
numberArray.append(thirdNumber)
numberArray.append(fourthNumber)
numberArray.append(fifthNumber)

# Loop through array to see whether there is even numbers
# And put in the result array

resultArray = []

for numItens in numberArray:
    if numItens % 2 == 0:
        resultArray.append(numItens)

# Give the number of even numbers as string for our user

print(len(resultArray), 'valores pares')