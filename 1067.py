# Reads the input of the user

numberUser = int(input())

# Create a counter

countNumber = 0

# Print all the odd numbers between 0 and given number

while countNumber <= numberUser:
    if countNumber % 2 != 0:
        print(countNumber)
    countNumber += 1