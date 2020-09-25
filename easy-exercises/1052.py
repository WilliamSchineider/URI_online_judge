# Create dictionary of the months and its corresponded number

dictionaryMonth = {
    1:'January',
    2:'February',
    3:'March',
    4:'April',
    5:'May',
    6:'June',
    7:'July',
    8:'August',
    9:'September',
    10:'October',
    11:'November',
    12:'December'
}

# Read user's input

userQuery = int(input())

# Check user's query in the dictionary

for monthQ in dictionaryMonth:
    if userQuery == monthQ:
        print(dictionaryMonth[userQuery])