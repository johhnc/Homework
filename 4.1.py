# John Crosbie
# CIS 122
# Ch 4.1
# 02/19/18


# 4.1.2
print("Q2 is:")
def main():
    acres = 5 # number of acers in a parking lot
    print("You can park around", cars(acres), "cars on a five-acer lot")
def cars(n):
    numberOfCars = 100 * n
    return numberOfCars
main()

# 4.1.4
print("Q4 is:")
def main():
    num = 27
    if isEven(num):
        print(num, "is an even number.")
    else:
        print(num, "is an odd number.")
def isEven(n):
    if n // 2 == 0:
        return True
    else:
        return False
main()

# 4.1.6
print("Q6 is:")
def main():
    taxableIncome = 16000
    print("Your income tax is ${0:,.2f}".format(stateTax(taxableIncome)))
def stateTax(income):
    if income <= 15000:
        return .03 * income
    else:
        return 450 + (.049 * (income - 15000))
main()