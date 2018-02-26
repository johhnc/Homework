# John Crosbie
# CIS 122
# Ch 5.3
# 03/05/18

# 1-20 dictionary
NE = {"CT":3.6, "ME":1.3, "MA":6.5, "NH":1.5, "RI":1.1, "VT":0.6}
# 5.3.2
print("Q2 is:")
print(len(NE))

# 5.3.4
print("Q4 is:")
print(list(NE.values()))

# 5.3.6
print("Q6 is:")
print("NH" in NE)

# 5.3.8
print("Q8 is:")
print(NE.get("RI", "absent"))

# 5.3.10
print("Q10 is:")
print(min(NE))

# 5.3.12
print("Q12 is:")
del NE["ME"]
print(len(NE))

# 5.3.14
print("Q14 is:")
NE.clear()
print(NE)

# 5.3.16
# FUCKING DICKERED NOTHING RETURNS
print("Q16 is:")
for x in sorted(NE):
    print(x + " ", end="")

# 5.3.18
print("Q18 is:")
total = 0
for x in NE:
    total += NE[x]
print("{0:.1f}".format(total))

# 5.3.20
# FUCKING DICKERED!!!! KEY ERROR 'VT'
# print("Q20 is:")
# newEngland = dict(NE)
# del newEngland["VT"]
# print(len(NE))

