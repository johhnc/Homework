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
