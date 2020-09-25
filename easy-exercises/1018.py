# Read the user's input of banknotes

userBanknote = int(input()) # Maximum amount 1000000, minimum 0.
numberDigits = len(str(userBanknote)) # Count the number of digitCode
userBanknoteString = str(userBanknote) # Transform user's input into string

# Create function for number decomposition and change calculation

def ATMwithdraw (digitCode, userRequest):

    dictionaryOfDigits = {
        1:userRequest[0:1],
        2:userRequest[0:2],
        3:userRequest[0:3],
        4:userRequest[0:4],
        5:userRequest[0:5],
        6:userRequest[0:6]
    }

    if (digitCode >= 3):
        changeFor100 = dictionaryOfDigits

    """
    # Change calculation
     
    changeFor50 = 
    changeFor20 = 
    changeFor10 = 
    changeFor5 = 
    changeFor2 =
    changeFor1 = 
    """
    return dictionaryOfDigits[digitCode]

print(ATMwithdraw(numberDigits, userBanknoteString))

"""
5 nota(s) de R$ 100,00
1 nota(s) de R$ 50,00
1 nota(s) de R$ 20,00
0 nota(s) de R$ 10,00
1 nota(s) de R$ 5,00
0 nota(s) de R$ 2,00
1 nota(s) de R$ 1,00
"""