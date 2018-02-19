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


# 4.2.50
print("Q50 is:")
def main():
    grade = getAverageGrade()
    semGrade = calculateLetterGrade(grade)
    print("Semester grade:", semGrade)
def getAverageGrade():
    midGrade = int(input("Enter grade on midterm exam: "))
    finalGrade = int(input("Enter grade on final exam: "))
    return ceil((midGrade + 2 * finalGrade) / 3)
def ceil(x):
    if int(x) != x:
        return int(x + 1)
    else:
        return x
def calculateLetterGrade(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"
main()

# 4.2.52
print("Q52 is:")
def main():
    grades = []
    for i in range(1, 6):
        grade = eval(input("Enter grade " + str(i) + ": "))
        grades.append(grade)
    grades.sort()
    grades = grades[2:]
    (rng, ave) = analyzeGrades(grades)
    print("Range:", rng)
    print("Average:", ave)
def analyzeGrades(grades):
    rng = grades[-1] - grades[0]
    ave = sum(grades) / len(grades)
    return (rng, ave)
main()

# 4.2.54

print("Q54 is:")
def main():
    newEngland = [("Maine", 30840, 1.329), ("Vermont", 9217, .626), ("New Hampshire", 8953, 1.321),
          ("Massachusetts", 7800, 6.646), ("Connecticut", 4842, 3.59), ("Rhode Island", 1044, 1.05)]
    newEngland.sort(key=sortByPop, reverse=True)
    print("Sorted by population in descending order:")
    for state in newEngland:
        print(state[0], " ", end="")
def sortByPop(state):
    return state[2]
main()

# 4.2.56
print("Q56 is:")
def main():
    newEngland = [("Maine", 30840, 1.329), ("Vermont", 9217, .626), ("New Hampshire", 8953, 1.321),
          ("Massachusetts", 7800, 6.646), ("Connecticut", 4842, 3.59), ("Rhode Island", 1044, 1.05)]
    newEngland.sort(key=sortBySizeOfName)
    print("Sorted by length of name in ascending order:")
    for state in newEngland:
        print(state[0], " ", end="")
def sortBySizeOfName(state):
    return len(state[0])
main()

















