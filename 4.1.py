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

# 4.1.8
print("Q8 is:")
def main():
    times("best")
    times("worst")
def times(word):
    print("It was the", word, "of times.")
main()

# 4.1.10
print("Q10 is")
def main():
    commonFates()
    print("died")
    commonFates()
    print("survived")
def commonFates():
    print("divorced")
    print("beheaded")
main()

# 4.1.12
print("Q12 is:")
def main():
    listPres = getListOfPresidents()
    num = int(input("enter a number from 1 through 44:  "))
    print(listPres[num - 1], "was president number", num)
def getListOfPresidents():
    infile = open("USpres.txt", 'r')
    listPres = [line.rstrip() for line in infile]
    infile.close()
    return listPres
main()

# 4.1.14
print("Q14 is:")
x = 7
def main():
    global x
    x = 5
    f()
    print(x)
def f():
    print(x)
main()

# 4.1.16
print("Q16 is:")
word = "spam"
def main():
    f()
    print(word)
def f():
    global word
    word = word.upper()
main()

# 4.1.18
print("Q18 is:")
ESTATE_TAX_EXEMPTION = 1000000
TAX_RATE = .45

def main():
    valueOfEstate = 3000000
    tax = TAX_RATE * (valueOfEstate - ESTATE_TAX_EXEMPTION)
    print("You owe ${0:,.2f} in estate taxes.".format(tax))
main()

# 4.1.20
print("Q20 is:")
def main():
    word = "garb"
    reverseWord(word)
    print(word)
def reverseWord(word):
    list1 = list(word)
    list1.reverse()
    word = "".join(list1)
    print(word)
main()

# 4.1.22
print("Q22 is:")
def main():
    grades = [80, 75, 90, 100]
    grades = dropLowest(grades)
    average = sum(grades) / len(grades)
    print(round(average))
def dropLowest(grades):
    lowestGrade = min(grades)
    grades.remove(lowestGrade)
    return grades
main()

# 4.1.24
print("Q24 is:")
def main():
    quotation = input("Enter a quotation:   ")
    print("\nMENU")
    print(" 1. Count number of vowels in the quotation. ")
    print(" 2. count number of uppercase letters in the quotation.  ")
    choice = int(input("Select 1 or 2 from the menu:  "))
    if choice == 1:
        print("Number of vowels:", calculateNumberOfVowels(quotation))
    else:
        print("Number of uppercase letters:", calculateNumberOfCaps(quotation))
def calculateNumberOfVowels(quotation):
    numberOfVowels = 0
    for ch in quotation:
        if ch.upper() in "AEIOU":
            numberOfVowels += 1
        return numberOfVowels
def calculateNumberOfCaps(quotation):
    numberOfCaps = 0
    for ch in quotation:
        if 'A' <= ch <= 'Z':
            numberOfCaps += 1
        return numberOfCaps
main()

# 4.1.26
print("Q26 is:")
def howMany(st1, st2):
    if st2 != "":
        n = 0
        i = 0
    while i < len(st1):
        if st1[i:].startswith(st2):
            n += 1
            i = i + len(st2)
        else:
            i += 1
        return n
    else:
        return len(st1) + 1

# 4.1.30
print("Q30 is:")
def main():
    first = getFirstName()
    last = getLastName()
    salary = getCurrentSalary()
    newSalary = calculateNewSalary(salary)
    displayResult(first, last, newSalary)
def getFirstName():
    first = input("Enter first name: ")
    return first
def getLastName():
    last = input("Enter last name: ")
    return last
def getCurrentSalary():
    salary = float(input("Enter current salary: "))
    return salary
def calculateNewSalary(salary):
    if salary < 40000:
        return (salary * 1.05)
    else:
        return 2000 + salary + (.02 * (salary - 40000))
def displayResult(first, last, newSalary):
    print("New salary for {0} {1}: ${2:,.2f}".format(first, last, newSalary))
main()

# 4.1.32
print("Q32 is:")
months = []
def main():
## display months containing the letter r.
    global months
    fillList()
    months = deleteNoRs()
    displayMonths()
def fillList():
    global months
    infile = open("Months.txt", 'r')
    months = [line.rstrip() for line in infile]
    infile.close
def deleteNoRs():
    reducedList = []
    for i in range(12):
        if 'r' in months[i].lower():
          reducedList.append(months[i])
    return reducedList
def displayMonths():
    print("The R months are:")
    print((", ").join(months))
main()