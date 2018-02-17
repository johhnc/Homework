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

