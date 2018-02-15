# John Crosbie
# CIS 122
# Ch 3.3
# 02/12/18

# 3.3.2
print("Q2 is:")
num = 3
while num < 15:
    num += 5
print(num)

# 3.3.4
print("Q4 is:")
total = 0
num = 1
while num < 5:
    total += num
    num += 1
print(total)

# 3.3.6
print("Q6 is:")
oceans = ["Atlantic", "Pacific", "Indian", "Arctic", "Antarctic"]
i = len(oceans) - 1
while i >= 0:
    if len(oceans[i]) < 7:
        del oceans[i]
    i = i - 1
print(", ".join(oceans))

# 3.3.8
print("Q8"
      "")
numTries = 0
year = 0
while (numTries < 7) and (year != 1964):
    numTries += 1
    year = int(input("Try #" + str(numTries) + ": In what year " + "did the Beatles invade the U.S?? "))

    if year == 1964:
        print("\nYes. They performed on the Ed Sullivan show in 1964.")
    elif year < 1964:
        print("Later than", year)
    else: # year > 1964:
        print("Earlier than", year)
if (numTries == 7) and (year != 1964):
    print("\nYour 7 tries are up. The answer is 1964")

# 3.3.16
print("Q16 is:")
restitution = float(input("Enter coefficient of restitution: "))
height = float(input("Enter initial height in meters: "))
# meters to centimeters
height *= 100
traveled = 0
# first bounce
bounces = 1
traveled = height
while height * restitution >= 10:
    bounces += 1
    height = restitution * height
    traveled += 2 * height
# centimeters to meters
traveled /= 100
print("Number if bounces:", bounces)
print("Meters traveled: {0:,.2f}".format(traveled))

# 3.3.18
print("Q18 is:")
factors = []
n = int(input("Enter a positive integer (> 1): "))
f = 2
while n > 1:
    if n // f == n / f:
        factors.append(str(f))
        n = n // f
    else:
        f += 1
result = " ".join(factors)
print("Prime factors are", result)

# 3.3.20
print("Q20 is:")
startYear = 2011 # as of October 21, 2011
population = 7 # population is 7 billion
while population <= 8:
    population = 1.011 * population
    startYear += 1
print("World population will be \n8 billion in the year", str(startYear) + ".")

