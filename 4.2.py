# John Crosbie
# CIS 122
# Ch 4.2
# 02/19/18

# 4.2.2
print("Q2 is:")
def main():
    ## Good advice to follow
    advice()
def advice():
    print("Keep cool, but dont freeze.")
    source()
def source():
    print("Source: A jar of Mayonnaise.")
main()

# 4.2.4
print("Q4 is:")
def main():
    grade = int(input("Enter your numeric grade:    "))
    showResult(grade)
def showResult(grade):
    if passedExam(grade):
        print("you passed with a grade of", str(grade) + '.')
    else:
        print("You failed the exam")
def passedExam(grade):
    if grade >= 60:
        return True
    else:
        return False
main()

# 4.2.6
print("Q6 is:")
def main():
    n, yob = getNameAndYOB()
    print(n, "will be", 2020- yob, "years old in 2020.")
def getNameAndYOB():
    name = input("Enter a name: ")
    yearOfBirth = int(input("Enter a year of birth: "))
    return name, yearOfBirth
main()

# 4.2.8
print("Q8 is:")
list1 = ["pear", "Banana", "apple"]
list1.sort()
print(list1)
list1.sort(key=lambda x: x.upper())
print(list1)

# 4.2.10
print("Q10 is:")
def main():
    for i in range(3):
        print(func())
def func(x=[]):
    x.append("wink")
    return x
main()

# 4.2.12
print("Q12 is:")



























