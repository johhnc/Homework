def main():
    firstName = getFirstName()
    lastName = getLastName()
    salary = getCurrentSalary()
    newSalary = calculateNewSalary(salary)
    displayResult(firstName, lastName, newSalary)
def getFirstName():
    firstName = input("Enter first name: ")
    return firstName
def getLastName():
    lastName = input("Enter last name: ")
    return lastName
def getCurrentSalary():
    salary = float(input("Enter current salary: "))
    return salary
def calculateNewSalary(salary):
    if salary < 40000:
        return (salary * 1.05)
    else:
        return 2000 + salary + (.02 * (salary - 40000))
def displayResult(firstName, lastName, newSalary):
    print("New salary for {0} {1}: ${2:,.2f}".format(firstName, lastName, newSalary))
main()