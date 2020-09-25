# Read three values

A, B, C = input().split()

A = float(A)
B = float(B)
C = float(C)

# Perform all the calculations

areaTriangle = (A * C) / 2 # Base A and height C
areaCircle = 3.14159 * C**2 # radius C (pi = 3.14159)
areaTrapezium = ((A + B) / 2) * C # A and B by Base and C by height
areaSquare = B**2 # Side B
areaRectangle = A * B # Sides A and B

# Print the results

print('TRIANGULO:', format(areaTriangle, '.3f'))
print('CIRCULO:', format(areaCircle, '.3f'))
print('TRAPEZIO:', format(areaTrapezium, '.3f'))
print('QUADRADO:', format(areaSquare, '.3f'))
print('RETANGULO:', format(areaRectangle, '.3f'))