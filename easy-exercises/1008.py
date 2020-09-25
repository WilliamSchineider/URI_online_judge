# Reads employee's number, worked hours, amount received per hour.

employeeNumber = int(input())
workedHoursPerMonth = int(input())
receivedPerHour = float(input())

employeeSalary = workedHoursPerMonth * receivedPerHour

print('NUMBER =', employeeNumber)
print('SALARY = U$', format(employeeSalary, '.2f'))