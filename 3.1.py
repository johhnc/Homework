# John Crosbie
# CIS 122
# Ch 3.1
# 02/05/18


# 3.1.2
print("Q2 is:")
print('C' + chr(35))

# 3.1.4
print("Q4 is:")
print(chr(ord('B'))) #the ASCII Value of B is 66

# 3.1.6
print("Q6 is:")
list1 = [17, 3, 12, 9, 10]
list1.sort()
print("Minimum:", list1[0])
print("Maximum:", list1[-1])

# 3.1.8
print("Q8 is:")
letter = 'D'
spread = ord('a') - ord('A')
print(chr(ord(letter) + spread))

# values for 9-20
a = 2
b = 3

# 3.1.10
print("Q10 is:")
print(((5 - a) * b) < 7)

# 3.1.12
print("Q12 is:")
print(a ** b == b ** a)

# 3.1.14
print("Q14 is:")
print(3e-2 < .01 *a)

# 3.1.16
print("Q16 is:")
print((a * a < b) or not(a * a < a))

# 3.1.18
print("Q18 is:")
print(not(a < b) or not (a < (b + a)) )

# 3.1.20
print("Q20 is:")
print(((a == b) or not (b < a)) and ((a < b) or (b == a + 1)))

# 3.1.22
print("Q22 is:")
print("Inspector" < "gadget")

# 3.1.24
print("Q24 is:")
print('J' >= 'J')

# 3.1.26
print("Q26 is:")
print('B' > '?')

# 3.1.28
print("Q28 is:")
print("Duck" < "Duck" + "Duck")

# 3.1.30
print("Q30 is:")
print("th" in "Python")

# 3.1.32
print("Q32 is:")
print((7 <34) and ("7" < "34"))

# 3.1.34
print("Q34 is:")
print(isinstance(32., int))

# 3.1.36
print("Q36 is:")
print(isinstance(32, int))

# 3.1.38
print("Q38 is:")
print("knight".startswith('n'))

# 3.1.40
print("Q40 is:")
print("flute".endswith('t'))

# 3.1.42
print("Q42 is:")
print(True and False)

# 3.1.44
print("Q44 is:")
print(not False)

# 3.1.46
print("Q46 is:")
print(not(a < b))
print(a > b)
print("Equivalent")

# 3.1.48
print("Q48 is:")
print(not(a == b) or (a == c))
print((a != b) or (a != c))
print("Equivalent")

# 3.1.50
print("Q50 is:")
print((a < b) and ((a > d) or (a > e)))
print((a < b) and (a > d) or ((a < b) and (a > e)))

