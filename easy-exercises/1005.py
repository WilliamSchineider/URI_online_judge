# Read two floating points (student's grade)

A = float(input())
B = float(input())

# Weight of grades (A -> 3.5 and B -> 7.5)
# Calculate the avarage

MEDIA = format((A * 3.5 + B * 7.5)/(3.5 + 7.5), '.5f')

print('MEDIA =', MEDIA)