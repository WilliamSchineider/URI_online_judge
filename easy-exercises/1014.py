# Read user's input

totalDistance = int(input())
spentFuel = float(input())

# Calculate the fuel consumption and print it

avarageFuelConsumption = totalDistance/spentFuel

print(format(avarageFuelConsumption, '.3f'),'km/l')