# Read the coordinates of two points

x1, y1 = input().split()
x2, y2 = input().split()

x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)

# Calculate the distance between the two points

pointsDist = ((x2-x1)**2+(y2-y1)**2)**(1/2)

# Output the result

print(format(pointsDist, '.4f'))