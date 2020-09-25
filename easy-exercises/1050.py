# Create a dictionary with all Area Codes

dictionaryCode = {        
        61:'Brasilia',
        71:'Salvador',
        11:'Sao Paulo',
        21:'Rio de Janeiro',
        32:'Juiz de Fora',
        19:'Campinas',
        27:'Vitoria',
        31:'Belo Horizonte'
    }

# Read user's input

areaCode = int(input())

# Check whether the code exist in the dictionary or is not found

for codes in dictionaryCode:
    if areaCode == codes:
        print(dictionaryCode[areaCode])

if dictionaryCode.get(areaCode) == None:
    print('DDD nao cadastrado')