# John Crosbie
# CIS 122
# Ch 5.1
# 02/26/18

# 5.1.2
print("Q2 is:")
outfile = open("Greetings.txt", 'w')
outfile.write("Hello\n")
outfile.write("Aloha\n")
outfile.close()
infile = open("Greetings.txt", 'r')
text = infile.readline().rstrip()
infile.close()
print(text)

# 5.1.4
print("Q4 is:")
list1 = ["Hello", "Aloha\n"]
outfile = open("Greetings.txt", 'a')
outfile.writelines(list1)
outfile.close()
infile = open("Greetings.txt", 'r')
text = infile.read().rstrip()
infile.close()
print(text)

# 5.1.6
print("Q6 is:")
print(sorted([x ** 2 for x in range(-2, 3)]))

# 5.1.8
print("Q8 is:")
print(sorted({x ** 2 for x in range(-2, 3)}))

# 5.1.10
print("Q10 is:")
s = {"Always", "up.", "give", "Never"}
s.discard("Always")
print(" ".join(sorted(s, key=len, reverse=True)))

# 5.1.12
print("Q10 is:")
s = set("dozen")
s.discard('d')
print(sorted(s, reverse=True))

# Commands for 23 and 24
# import os.path
# if os.path.isfile("ABC1.txt"):
#    print("File already exists.")
# else:
#    infile = open("ABC1.txt", 'w')
#    infile.write("a\nb\nc\n")
#    infile.close()

# 5.1.24
print("Q12 is:")
print("File already exists. is printed")

# 5.1.34
print("Q34 is:")
def main():
    number = getNumbers("Numbers.txt")
    print("The file Numbers.txt contains", number, "numbers.")

def getNumbers(filename):
    infile = open("Numbers.txt", 'r')
    number = 0
    for line in infile:
        number += 1
    infile.close()
    return number
main()

# 5.1.36
print("Q36 is:")
def main():
    small = getSmall("Numbers.txt")
    print("The smallest number in the file Numbers.txt is",
    str(small) + ".")

def getSmall(fileName):
    infile = open("Numbers.txt", 'r')
    min = int(infile.readline())
    for line in infile:
        num = int(line)
    if num < min:
        small = num
    infile.close()
    return min
main()

# 5.1.38
print("Q38 is:")
def main():
    ave = getAve("Numbers.txt")
    print("The average of the numbers in \nthe file Numbers.txt is {0:,.1f}.".format(ave))

def getAve(fileName):
    infile = open("Numbers.txt", 'r')
    sum = 0
    quantity = 0
    for line in infile:
        sum += int(line)
        quantity += 1
    infile.close()
    return sum / quantity
main()

# 5.1.40
print("Q40 is: See Code")
import os
def main():
    infile = open("SomeMonths.txt", 'r')
    outfile = open("Temp.txt", 'w')
    for month in infile:
        if 'r' not in month.lower():
            outfile.write(month)
    infile.close()
    outfile.close()
    os.remove("SomeMonths.txt")
    os.rename("Temp.txt", "SomeMonths.txt")

main()

# 5.1.42
print("Q42 is: see code")
import os
def main():
    infile = open("SomeStates.txt", 'r')
    outfile = open("Temp.txt", 'w')
    for state in infile:
        if state[:1] not in "AEIOU":
            outfile.write(state)
    infile.close()
    outfile.close()
    os.remove("SomeStates.txt")
    os.rename("Temp.txt", "SomeStates.txt")
main()

# 5.1.44
infile = open("PresStates.txt", 'r')
statesSet = {state.rstrip() for state in infile}
infile.close()
print(len(statesSet), "different states have produced presidents of the United States.")

