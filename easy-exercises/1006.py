# Read three values A, B and C (Student's grades)

A = float(input())
B = float(input())
C = float(input())

# Weight of grades A -> 2, B -> 3 and C -> 5

MEDIA = format((A * 2 + B * 3 + C * 5)/(2 + 3 + 5), '.1f')

print('MEDIA =', MEDIA)