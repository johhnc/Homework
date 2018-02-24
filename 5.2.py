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
