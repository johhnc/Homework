# John Crosbie
# CIS 122
# Ch 2.4
# 1/29/18

states = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
          "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont",
          "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine",
          "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota",
          "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota",
          "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# 2.4.2
print("Q2 is:")
print(states[2], states[-2])

# 2.4.4
print("Q4 is:")
print(len(states))

# 2.4.6
print("Q6 is:")
print(states.index("Delaware"))

# 2.4.8
print("Q8 is:")
print(states.index(states[-2]))

# 2.4.10

print("Q10 is:"), print(states[len(states) - 1], states[-1])

# 2.4.12
print("Q12 is:"), print(states.append("Puerto Rico")), print(states[50])

# 2.4.14
print("Q14 is:")
del states[2]
print(states[2])

# 2.4.16
print("Q16 is:")
del states[22]
print(states.index("Hawaii"))

# 2.4.18
print("Q18 is:")
print(states[1:4])

# 2.4.20
print("Q20 is:")
print(states[-4:-1])

# 2.4.22
print("Q22 is:")
print(states[:1])

# 2.4.24
print("Q24 is:")
print(states[-2:])

# 2.4.26
print("Q26 is:")
print(states[-1:4])

# 2.4.28
print("Q28 is:")
print(states[-12:][-3])

# 2.4.30
print("Q30 is:")
print(states[:][5])

# 2.4.32
print("Q32 is:")
print(states[:][2])

# 2.4.34
print("Q34 is:")
print(len(states[-30:]))

# 2.4.36
print("Q36 is:")
print(len(states[:]))

# 2.4.38
print("Q38 is:")
print(len(states[2:-2]))

# 2.4.40
print("Q40 is:")
states.append(["Puerto Rico", "Guam"])
print(states[-3:])

# 2.4.42
print("Q42 is:")
del states[-2]
states.insert(-1, "Sewards's Folly")
print(states[-3:])

# 2.4.44
print("Q44 is:")
del states[1]
states.insert(1, "Commonweath of Pennsylvania")
print(states[:3])

# 2.4.46
print("Q46 is: needs work")
#list2 = states[2].split() + states[-4].split()
#list2.remove("New")
#print(list2)

# 2.4.48
print("Q48 is:")
print((',').join(states[1:4]))

# list1 numbers
list1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
         "21", "22", "23", "24", "25", "26", "27", "28", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37",
         "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55",
         "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73",
         "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88", "89", "90", "91",
         "92", "93", "94", "95", "96", "97", "98", "99", "100"]

# 2.4.50
print("Q50 is:")
print(list1[:8])

# 2.4.52
print("Q50 is:")
print(list1[-8:-1])

#2.4.54
print("Q54 is:")
print(list1[1:-1])

# list for numbs
nums = [6, 2, 8, 0]

# 2.4.56
print("Q56 is:")
print("Length:", len(nums))

# 2.4.58
print("Q58 is: needs work")
#print("Number Lot:", sum(nums) / list(nums))

# 2.4.60
print("Q60 is:")
L = ["one", "for", "all"]
L[0], L[-1] = L[-1], L[0]
print(L)

# 2.4.62
print("62 is:")
name = input("Enter Name with three parts: ")
L = name.split()
print(L[0], L[2])

# 2.4.64
list1 = ['h','o', 'n', 'P', 'y', 't']
list2 = list1[3:] + list1[:3]
print(("".join(list2)))

# 2.4.68
print("Q68 is:")
carousel = ["merry", "go", "round"]
print(('-').join(carousel))

# 2.4.70
print("Q70 is:")
allDay = "around-the-clock"
print(allDay.split('-'))

# 2.4.72
print("Q72 is:")
nations = "France\nEngland\nSpain"
countries = nations.split()
print(countries)

# 2.4.74
print("Q74 is:")
infile = open("Abc.txt", 'r')
alpha = [line.rstrip() for line in infile]
infile.close()
word = ("".join(alpha))
print(word)

# 2.4.76
print("Q76 is:")
infile = open("Live.txt", 'r')
words = [line.rstrip() for line in infile]
infile.close()
words.append(words[0].lower())
quote = (" ").join(words) + '.'
print(quote)

# 2.4.78
print("Q78 is:")
nums = (6, 2, 8, 0)
print("Largest Number:", max(nums))
print("Length:", len(nums))
print("Total:", sum(nums))
print("Number List:", list(nums))

# 2.4.80
print("Q80 is:")
word = "Diary"
list1 = list(word)
list1.insert(3, list1[1])
del list1[1]
word = "".join(list1)
print(word)

# 2.4.82
print("Q82 is:")
nums = [-5, 17, 123]
print(tuple(nums))

# 2.4.84
print("Q84 is:")
t = (1, 2, 3)
t = (0,) + t[1:]
print(t)

# 2.4.86
print("Q86 is:")
list1 = ["soprano", "tenor"]
list2 = ["alto", "base"]
print(list1 + list2)

# 2.4.88
print("Q88 is:")
list1 = ["gold"]
list2 = ["silver", "bronze"]
list1.extend(list2)
print(list1 + list2)

# 2.4.90
print("Q90 is:")
list1 = [0]
print(list1 * 4)

# 2.4.92
print("Q92 is:")
ships = ["Nina", "Pinta", "Santa Maria"]
print(ships[-5:2])

# 2.4.102 -- works but retains punctuation
print("Q102 is:")
sentence = input("Enter a sentence: ")
print("First word:", sentence[:1])
print("Last word", sentence[-1:])

# 2.4.104
print("104 is:")
fullName = input("Enter a 3-part name: ")
name = fullName.split()
print("Middle Name: ", name[1])

# Programing Project 2
print("Programing Project 2 is:")
A = float(input("Enter amount of loan: "))
r = float(input("Enter intrest rate (%):  "))
n = float(input("Enter number of years:   "))
i = r / 1200
monthlyPayment = i / (1 - (1 + i) ** (-12 * n)) * A
monthlyPayment = round(monthlyPayment, 2)
print("Monthly Payment:", "$", monthlyPayment)

# Programing Project 4
print("Programing project 4 is:")
price = float(input("Price of item: "))
print("Enter weight of item in ponds and ounces separately")
pounds = int(input("Enter Pounds: "))
ounces = int(input("Enter Ounces: "))
pounds1 = pounds * 16
totalOunces = pounds1 + ounces
perOunce = price / totalOunces
print("Price Per Ounce:", "$" ,round(perOunce, 2))


















