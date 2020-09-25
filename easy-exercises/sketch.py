userBanknote = int(input()) # Maximum amount 999999, minimum 1.
userB = str(userBanknote) # Transform user's input into string

changeFor100 = int((int(userB[0:3]) - int(userB[1:3])) / 100)

print(changeFor100)


changeFor100 = (int(userB[0:6]) - int(userB[1:6])) / 100

print(changeFor100)
