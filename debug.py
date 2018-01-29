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



