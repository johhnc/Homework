# John Crosbie
# CIS 122
# Ch 5.1
# 02/19/18

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
outfile.open("Greetings.txt", 'a')
outfile.writelines(list1)
outfile.close()
infile.open("Greetings.txt", 'r')
text = infile.read().rstrip()
infile.close()
print(text)

