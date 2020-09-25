# Read the distance in km from user

distanceKm = int(input())

# Calculate the time for car Y to be Zkm away from car X (x -> 60km/h and y -> 90km/h)

timeSpent = int((60 * distanceKm)/30)

print(timeSpent, 'minutos')