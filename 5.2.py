# John Crosbie
# CIS 122
# Ch 5.2
# 02/26/18

# 5.2.6
print("Q6 is:")
def main():
    countries = placeDataIntoList("UN.txt")
    countries.sort(key=byContinent)
    createFile(countries)
def placeDataIntoList(filename):
    listOfInfo = []
    infile = open(filename, 'r')
    line = infile.readline()
    while line.startswith('A'):
        line2 = line.split(',')
        listOfInfo.append(list((line2[0], line[2])))
        line = infile.readline()
    infile.close()
    return listOfInfo
def byContinent(country):
    return country[1]
def createFile(countries):
    outfile = open("CountriesByContinent.txt", 'w')
    for country in countries:
        outfile.write(country[0] + ',' + str(country[1]) + "\n")
    print("the lines of the new file contains the name of a country in Europe and its population in millions.\n"
      "The countries are in order by population. The first two countries in the file are Algeria and Angola" )
main()

# 5.2.8
print("Q8 is:")
def main():
    list = insertDataInList("DOW.txt")
    list.sort(key=byPercentGrowth)
    increase = (float(list[-1][5]) - float(list[-1][4])) / \
               float(list[-1][4])
    print("Best performing stock: {0:1} {1:0,.2f}%".
    format(list[-1][0], 100 * increase))
    increase = (float(list[0][5]) - float(list[0][4])) / \
                float(list[0][4])
    print("Worst performing stock: {0:1} {1:0,.2f}%".
    format(list[0][0], 100 * increase))
def insertDataInList(fileName):
    infile = open(fileName, 'r')
    lists = [line.rstrip() for line in infile]
    infile.close()
    for i in range(len(lists)):
        lists[i] = lists[i].split(',')
        lists[i][4] = eval(lists[i][4])
        lists[i][5] = eval(lists[i][5])
        lists[i][6] = eval(lists[i][6])
        lists[i][7] = eval(lists[i][7])
    return lists
def byPercentGrowth(stock):
    percentIncrease = (float(stock[5]) - float(stock[4])) / float(stock[4])
    return percentIncrease
main()

# 5.2.10
print("Q10 is:")
def main():
    stocks = dataIntoList("DOW.txt")
    stocks.sort(key=endOfYearPrice)
    display(stocks)
def dataIntoList(fileName):
    infile = open(fileName, 'r')
    lines = [line.rstrip() for line in infile]
    infile.close()
    for i in range(len(lines)):
        lines[i] = lines[i].split(',')
        lines[i][4] = eval(lines[i][4])
        lines[i][5] = eval(lines[i][5])
        lines[i][6] = eval(lines[i][6])
        lines[i][7] = eval(lines[i][7])
    return lines
def endOfYearPrice(stock):
    return stock[5]
def display(stockList):
    print("{0:20} {1:8} {2:s}".format("Company", "Symbol", "Price on 12/31/2013"))
    for i in range(5):
        print("{0:20} {1:8} ${2:0.2f}".format(stockList[i][0], stockList[i][1], stockList[i][5]))
main()

# 5.2.12
print("Q12 is:")
infile = open("Justices.txt", 'r')
supremeCourt = [line for line in infile if (int(line.split(',')[5]) == 0)]
supremeCourt.sort(key=lambda x: int(x.split(',')[4]))
print("Current Justices")
for justice in supremeCourt:
    print(justice.split(',')[0], justice.split(',')[1])

# 5.1.14
# its fucking DICKERED!!!! line 102 is tosing an error right now
print("Q14 is:")


def main():
    state = input("Enter a state abbreviation: ")
    justices = getJusticesByState(state)
    fix(justices)
    justices.sort(key=lambda justice1: str[5] - str[4], reverse=True)
    print("\n{0:18} {1:20}  {2}".format("Justice", "Appointing Pres", "Yrs Served"))
    for justice2 in justices:
        print("{0:18} {1:20}  {2}".format(justice2[0] + " " + justice2[1], justice2[2].split(" ")[-1],
                                          justice2[5] - justice2[4]))


def getJusticesByState(state):
    infile = open("Justices.txt", 'r')
    records = [line for line in infile if line.split(',')[3] == state]
    infile.close()
    for i in range(len(records)): records[i] = records[i].split(',')
    records[i][4] = int(records[i][4])
    records[i][5] = int(records[i][5])
    return records


def fix(justices):
    for justice in justices:
        if justice[5] == 0:
            justice[5] = 2015
main()

