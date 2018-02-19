# John Crosbie
# CIS 122
# Ch 4.2
# 02/19/18

# 4.2.2
print("Q2 is:")
def main():
    # Good advice to follow
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

def main():
    x, y = getTwoIntegers()
    x, y = calculateSumAndProduct(x, y)
    displaySumAndProduct(x, y)
def getTwoIntegers():
    a = int(input("Enter first integer: "))
    b = int(input("Enter second integer:    "))
    return a, b
def calculateSumAndProduct(x, y):
    return x + y, x * y
def displaySumAndProduct(x, y):
    print("Sum" + ':', x)
    print("Product" + ':', y)
main()

# 4.2.14
print("Q14 is:")
def main():
    composers = ["Johann Sebastian Bach", "Wolfgang Amadeus Mozart", "Franz Joseph Haydn", "Ralph Vaughn Williams"]
    composers.sort(key=lengthOfLastName)
    for composer in composers:
        print(composer)
def lengthOfLastName(composer):
    compList = composer.split
    return len(compList[-1])
main()


# 4.2.16
print("Q16 is:")

def main():
    list1 = ["e", "pluribus", "unum"]
    list2 = sorted(list1, key=numberOfVowels)
    print(list2)
def numberOfVowels(word):
    return len([ch for ch in word if (ch in "aeiou")])
main()

# 4.2.18
print("Q18 is:")

popularLaguages = ["Python", "C", "C++", "Ruby", "VB", "PHP"]
for item in sorted(popularLaguages):
    print(item, end="   ")

# 4.2.20
print("Q20 is:")
popularLaguages = ["Python", "C", "C++", "Ruby", "VB", "PHP"]
for item in sorted(popularLaguages, key=len):
    print(item, end=" ")

# 4.2.22
print("Q22 is:")

numbers = [4, 6, -2, -3, 5]
for num in sorted(numbers):
    print(num, end="  ")

# 4.2.24
print("Q24 is:")

popLaguages = ["Python", "C", "C++", "Ruby", "VB", "PHP"]
sentence = "I program in VB, Python, and Ruby"
list1 = sentence.split()
myLanguages = [word[:-1] for word in list1 if word[:1] in popLaguages]
for language in myLanguages:
    print(language, end="   ")























