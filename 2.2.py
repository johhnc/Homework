# John Crosbie
# CIS 122
# Ch 2.2
# 1/22/18


# Q2.2.2
print("Q2 is:", "Hello")

# Q2.2.4
var = "Bert"
print("Q4 is:", var)

# Q2.2.6
print("Q6 is:", "Python"[-2])

# Q2.2.8
print("Q8 is:", "Python"[5])

# Q2.2.10
print("Q10 is:", "Python"[2:2])

# Q2.2.12
print("Q12 is:", "Python"[2:])

# Q2.2.14
print("Q14 is:", "Python"[-5:-1])

# Q2.2.16
print("Q16 is:", "Python"[-4:4])

# Q2.2.18
print("Q18 is:", "Python"[-10:10])

# Q2.2.20
print("Q20 is:", "Python".find("ty"))

# Q2.2.22
print("Q22 is:", "Python".find("Pyt"))

# Q2.2.24
print("Q24 is:", "whippersnapper".find("pp"))

# Q2.2.26
print("Q26 is:", "Mississippi".rfind("ss"))

# Q2.2.28
print("Q28 is:", "Moscow".rfind("k"))

# Q2.2.30
print("Q30 is:", "brrr".upper())

# Q2.2.32
print("Q32 is:", len("brrr"))

# Q2.2.34
print("Q34 is:", "whippersnapper".count("pp"))

# Q2.2.36
print("Q36 is:", "Python".lower())

# Q2.2.38
print("Q38 is:", len("Gravity   ".rstrip()))

# Q2.2.40
print("Q40 is:", "king lear".title())

# Q2.2.42
print("Q42 is", "Hello World!".lower().find('wo'))

# Q2.2.44
print("Q44 is:", "Python".upper().find("tho"))

# Q2.2.46
print("Q46 is:", "all clear".title().count('a'))

# Q2.2.48
m = 4
n = 3
s = "Microsoft"
t = "soft"

print("Q48 is:")
print(len(s)), print(s.lower()), print(s[m:m + 2]), print(s.find(t))

# Q2.2.50

print("Q50 is:"), print("a" + "cute")

# Q2.2.52

print("Q52 is:") ,print("Fred has " + str(2) + " children.")

# Q2.2.54

sentence = "ALPHONSE TIPPYTOED AWAY."
print("Q54 is:"),print(sentence[12:15] + sentence[3:6])

# Q2.2.56

strl = "mur"
strl += strl
print("Q56 is:"), print(strl)

# Q2.2.58

var = "eight"
var += "h"
print("Q58 is:"), print(var)

# Q2.2.60
print("Q60 is:"), print(('*' * 3) + "YES" + ('*' * 3))

# Q2.2.62
print("Q62 is:")
print("spam" * 4)

# Q2.2.64
print("Q64 is:")
str1 = "5"
num = 0.5 + int(str1)
print(num)

# Q2.2.66
print("Q66 is:")
num = int(input("Enter an integer:  "))
print(1 + num)

# Q2.2.68

print("Q68 is:")
num = eval(input("Enter a number:   "))
print(1 + num)

# Q2.2.70
batmanAndRobin = "THE DYNAMIC DUO".lower().title()
print("Q70 is:"), print(batmanAndRobin)

# Q2.2.94
item = "ketchup"
regularPrice = float(1.80)
discount = float(.27)
print("Q94 is:", "$", regularPrice - discount, "is the sale price of", item)

# Q2.2.96
prefix = "Fore"
print("Q96 is:"), print(prefix + "warned", "is", prefix + "armed.")

# Q2.2.98
print("Q98 is:")
a = int(input("Enter Your Age:  "))
r = int(input("Enter Your Resting Heart Rate:   "))
beats = .7 * (220 - a) + .3 * r
beats = round(beats)
print("Your Training Heart Rate is:"), print(beats, "beats/min")

# Q2.2.100
print("Q100 is:")
wattage = int(input("Enter wattage: "))
hoursUsed = int(input("Enter the number of hours used: "))
costPerKWH = float(input("Enter the cost per kWh in cents:  "))
costOfElectricity = (wattage * hoursUsed) / (1000 * costPerKWH)

print("", "$", round(costOfElectricity, 2))


