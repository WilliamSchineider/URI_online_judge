# Reads saller's name, fixed salary and total sales made by her/him

sallerName = str(input())
fixedSalary = float(input())
totalMadeMonth = float(input())

# Total amount paid with bonus

totalPaidWBonus = fixedSalary + totalMadeMonth * 0.15

# Output of the total to be paid

print('TOTAL = R$', format(totalPaidWBonus, '.2f'))