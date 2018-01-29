# Programing Project 2
print("Programing Project 2 is:")
A = float(input("Enter amount of loan: "))
r = float(input("Enter intrest rate (%):  "))
n = float(input("Enter number of years:   "))
i = r / 1200
monthlyPayment = i / (1 - (1 + i) ** (-12 * n)) * A
monthlyPayment = round(monthlyPayment, 2)
print("Monthly Payment:", "$", monthlyPayment)



