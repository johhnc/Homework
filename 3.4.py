# John Crosbie
# CIS 122
# Ch 3.4
# 02/12/18

# 3.4.2
print("Q2 is:", range(-11, -7))

# 3.4.4
print("Q4 is:", range(2010, 2030, 5))


# 3.4.6
print("Q6 is:", range(1))


# 3.4.8
print("Q8 is:", range(12, 2, -5))


# 3.4.10
print("Q10 is:")
print("range(4)")

# 3.4.12
print("Q12 is:")
print("range(4, 0, -1)")

# 3.4.14
print("Q14 is:")
print("range(7, 8)")

# 3.4.18
print("Q18 is:")
for i in range(3 ,2):
    print(2 * i)

# 3.4.20
print("Q20 is:")
for i in range(-9, 0, 3):
    print(i)

# 3.4.22
print("Q22 is:")
n = 3
total = 0
for i in range(1, n + 1):
    total += 1
print(total)

# 3.4.24
print("Q24 is:")
for countdown in range(10, 0, -1):
    print(countdown)

# 3.4.26
print("Q26 is:")
numCaps = 0
name = "United States of America"
for ch in name:
    if ch.isupper():
        numCaps += 0
print(numCaps)

# 3.4.28
print("Q28 is:")
word = "cloudier"
newWord = ""
evenIndex = True
for ch in word:
    if evenIndex:
        newWord += ch
    evenIndex = not evenIndex
print(newWord)

# 3.4.30
print("Q30 is:")
for ch in "Python":
    break
print(ch)

# 3.4.32
print("Q32 is:")
list1 = [2, 9, 6, 7, 13, 3]
maxOfOdds = 0
for num in list1:
    if (num % 2 == 1) and (num > maxOfOdds):
        maxOfOdds = num
print(maxOfOdds)

# 3.4.34
print("Q34 is:")
numOfNumbers = 0
list1 = ["three", 4, 5.7, "six", "seven", 8, 3.1416]
for item in list1:
    if isinstance(item, str):
        continue
    numOfNumbers
print(numOfNumbers)

# 3.4.36
print("Q36 is:")
# I'm looking over a four leaf clover.
leaves = ("sunshine", "rain", "the roses that bloom in the lane", "somebody I adore")
number = 1
for leaf in leaves:
    print("Leaf", str(number) + ':', leaf)
    number += 1

# 3.4.38
dataList = []
infile = open("Numbers.txt", 'r')






















