# John Crosbie
# CIS122
# Ch 2.3
# 1/22/18


# Q2.3.2

print("Q2 is:")
print("Price:  ", '$', 23.45, sep="")

# Q2.3.4

print("Q2 is:")
print("Py", "th", "on", sep="")

# Q2.3.6
print("Q3 is:")
print("tic", "tac", "toe", sep='-')

# Q2.3.8
print("Q8 is:")
print("one", "two", "three", sep=',')

# Q2.3.10
print("Q10 is:")
print("spam", end=" and ")
print("eggs")

# Q2.3.12
print("Q12 is:")
print("on", "site", sep='-', end="")
print("repair")

# Q2.3.14
print("Q14 is:")
print("Hello\n", end="")
print("World!")

# Q2.3.16
print("Q16 is:")
print("1\t2\t3")
print("Detroit\tLions")
print("Indianapolis\tColts")

# Q2.3.18
print("Q18 is:")
print("COUNTRY\t", "LAND AREA")
print("India\t", 2.5, "million sq km")
print("China\t", 9.6, "million sq km")

# Q2.3.20
print("Q20 is:")
print("STATE\tCAPITAL".expandtabs(15))
print("North Dakota\tBismarck".expandtabs(15))
print("South Dakota\tPierre".expandtabs(15))

# Q2.3.22
print("Q22 is:")
print("01234567890")
print("A".rjust(5), "B".center(5), "C".ljust(5), sep="")

# Q2.3.24
print("Q24 is:")
print("01234567890")
print("{0:>5s} {1:^5s} {2:5s}".format("A", "B", "C"))

# Q2.3.26
print("Q26 is:")
print("01234567890")
print("{0:10,d}".format(1234))
print("{0:^10,d}".format(1234))
print("{0:<10,d}".format(1234))

# Q2.3.28
print("Q28 is:")
print("{0:,.0f}".format(1234.567))

# Q2.3.30
print("Q30 is:")
print("${0:,.2f}".format(1234))

# Q2.3.32
print("Q32 is:")
print("{0:14s}{1:s}".format("Major", "Percent of Students"))
print("{0:14s}{1:10.1%}".format("Biology", .062))
print("{0:14s}{1:10.1%}".format("Psychology", .054))
print("{0:14s}{1:10.1%}".format("Nursing", .047))

# Q2.3.34
print("Q34")
print("Be {0:s} - {1:s} else is taken.".format("yourself", "everyone"))

# Q2.3.36
print("Q36 is:")
print("And now for {0:s} completely {1:s}.".format("something", "different"))

# Q2.3.38
print("Q38 is:")
strl = "The chances of winning the {0:s} are 1 in {1:d}"
print(strl.format("Powerball Lottery", 175223510))

# Q2.3.40
print("Q40 is:")
pi = 3.1415926598 # to 11 decimal places
print("Pi is approximately {0:.5f}.".format(pi))

# Q2.3.42
print("Q42 is:")
strl = "In a randomly selected group of {0:d} people, the " + \
       "probability\nis {1:.2f} that 2 people have the same birthday."
print(strl.format(23, .0507397))

# Q2.3.44
print("Q44 is:")
strl = "{0:.0%} of the number of the U.S. Senate are from {1:s}."
print(strl.format(12 / 100, "New England"))

# Q2.3.46
print("Q46 is:")
#663267/3794000 is .1748199789 to 10 decimal places
strl = "the area of {0:s} is {1:.1%} of the area of the U.S."
print(strl.format("Alaska", 663267 / 3794000))

# Q2.3.48
print("Q48 is:")
print("When you have {0:s} to {1:s}, {1:s} {0:s}.".format("nothing", "say"))

# Q2.3.50
print("Q50 is:")
strl = "if {0:s} dream it, {0:s} do it. - Walt Disney"
print(strl.format("you can"))

# Q2.3.52
print("Q52 is: ")
print("Hello\tWorld!")
print("Hello\tWorld!".expandtabs(8))
print("Yes the result is the same")

# Q2.3.54
print("Q54 is:")
revenue = int(input("Enter revenue: "))
expenses = int(input("Enter expenses: "))
netIncome = revenue - expenses

print("Net income: ${0:10,d}".format(netIncome))

# Q2.3.56
print("Q56 is:")
beginningSalary = float(input("Enter beginning salary: "))
newSalary = 1.15 * beginningSalary
percentChange = (newSalary - beginningSalary) / beginningSalary
print("New salary: ${0:,.2f}".format(newSalary))
print("Change: {0:.2%}".format(percentChange))

# Q2.3.58
print("Q58 is:")
f = float(input("Enter future value: "))
r = float(input("Enter interest rate (as %): "))
n = int(input("Enter number of years: "))
presentValue = f / (1 + (r / 100)) ** n
print("Present value: ${0:,.2f}".format(presentValue))


