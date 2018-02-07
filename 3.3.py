# John Crosbie
# CIS 122
# Ch 3.3
# 02/12/18

# 3.3.2
print("Q2 is:")
num = 3
while num <15:
    num += 5
print(num)

# 3.3.4
print("Q4 is:")
total = 0
num = 1
while num <5:
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

restitution = float(input("Enter coefficient of restitution: "))
height = float(input("Enter initial height in meters: "))
# meters to centimeters
height *= 100
distanceTraveled = 0
# first bounce
bounces = 1
distanceTraveled = height
while height * restitution >= 10:
    bounces += 1
height = restitution * height
distanceTraveled += 2 * height
# back to meters
distanceTraveled /= 100
print("Number if bounces:", bounces)
print("Meters traveled: {0:,.2f}".format(distanceTraveled))

