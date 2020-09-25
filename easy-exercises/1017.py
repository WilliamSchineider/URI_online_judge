# Read user's input: Spent Time [hours], Average Speed [km/h]

spentTime = int(input())
averageSpeed = int(input())

# Consunption calculation

consumptionFuel = float((averageSpeed * spentTime) / 12)

# Output result

print(format(consumptionFuel, '.3f'))