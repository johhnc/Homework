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

NE = {"CT":3.6, "ME":1.3, "MA":6.5, "NH":1.5, "RI":1.1, "VT":0.6}

# 5.3.16
print("Q16 is:")
for x in sorted(NE):
    print(x + " " )

# 5.3.18
print("Q18 is:")
total = 0
for x in NE:
    total += NE[x]
print("{0:.1f}".format(total))

# 5.3.20
print("Q20 is:")
newEngland = dict(NE)
del newEngland["VT"]
print(len(NE))

# dictionary for 21-44
homeRunKings = {"Bonds":762, "Aaron":755}
# 5.3.22
print("Q22 is:")
print(homeRunKings["Aaron"])

# 5.3.24
print("Q24 is:")
print(list(homeRunKings.items()))

# 5.3.26
print("Q26 is:")
print(max(homeRunKings))

# 5.3.28
print("Q28 is:")
print("Aaron" not in homeRunKings)

# 5.3.30
print("Q30 is:")
print(list(homeRunKings.keys()))

# 5.3.32
print("Q32 is:")
print(homeRunKings.get("Ruth", "NA"))

# 5.3.34
print("Q34 is:")
homeRunKings["Ruth"] = 714
print(homeRunKings)

# 5.3.36
print("Q36 is:")
homeRunKings["Bonds"] += 1
print(homeRunKings)

# 5.3.38
print("Q38 is:")
for x in homeRunKings.keys():
    print(x)

# 5.3.40
print("Q40 is:")
for x in sorted(homeRunKings):
    print(x)

# 5.3.42
print("Q42 is:")
dupHKRs = homeRunKings
dupHKRs["Bonds"] = 750
print(homeRunKings["Bonds"])

# 5.3.44
print("Q44 is:")
newHRKs = {}
newHRKs.update(homeRunKings)
print(newHRKs["Aaron"])

# 5.3.52
print("Q52 is:")


# 5.3.54
print("Q54 is:")


# 5.3.56
print("Q56 is:")


# 5.3.58
print("Q58 is:")

