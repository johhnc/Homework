# John Crosbie
# CIS 122
# Ch 3.2
# 02/05/18

# 3.2.2
print("Q2 is:")
gpa = 3.49
result = " "
if gpa >= 3.5:
    result = "Honors"
print(result + "Student")

# 3.2.4
print("Q4 is:")
print('A' < 'B' < 'c')

# 3.2.6
print("Q6 is:")
change = 356
if change >= 100:
    print("your change contains", change // 100, "dollars.")
else:
    print("you change contains no dollars.")

# 3.2.8
print("Q8 is:")
length = eval(input("Enter length of cloth in yards:    "))
if length < 1:
    cost = 3.00         #cost in dollars
else:
    cost = 3.00 + ((length - 1) * 2.50)
result = "Cost of cloth is #{0:0.2f}.".format(cost)
print(result)

# 3.2.10
print("Q10 is:")
isvowel = False
letter = input("Enter a Letter: ")
letter = letter.upper()
if (letter in "AEIOU"):
    isvowel = True
if isvowel:
    print(letter, "is a vowel.")
elif (not(65 <= ord(letter) <= 90)):
    print("You did not enter a letter")
else:
    print(letter, "is a vowel.")

# 3.2.12
print("Q12 is:")
number = 5
if number <0:
    print("Negative")
else:
    if number == 0:
     print("zero")
    else:
        print("positive")

# 3.2.14
print("Q14 is:")
if " ":
    print("An empty string is true")
else:
    print("An empty string is false")

# 3.2.24
print("Q24 is:")
feet = eval(input("How tall(in feet) is the Statue of Liberty?  "))
if (feet <= 141):
    print("Nope")
if (feet > 141):
    if (feet < 161):
        print("Good")
    else:
        print("Nope")

# 3.2.26
print("Q26 is:")
item = float(input("Enter the number of bagels: "))
if item < 6:
    cost = 0.75 * item
else:
    cost = .60 * item
print("The total cost for the bagels is ${0:,.2f}.".format(cost))

# 3.2.28
print("Q28 is:")
pages = int(input("Enter the number of copies:  "))
if pages < 100:
    cost = 0.05
else:
    cost = 5 + 0.03 * (pages - 100)
print("The total cost is ${0:,.2f}.".format(cost))

# 3.2.30
print("Q30 is:")
payRate = float(input("Enter your hourly wage: "))
hoursWorked = float(input("Enter number of hours you worked: "))
if hoursWorked <= 40:
    totalPay = payRate * hoursWorked
else:
    totalPay = (payRate * 40) + (1.5 * payRate * (hoursWorked - 40))
print("Your pay for week is ${0:,.2f}.".format(totalPay))
