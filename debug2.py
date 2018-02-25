def main():
    state = input("Enter a state abbreviation: ")
    judges = getJusticesByState(state)
    fixCurrentJudges(judges)
    judges.sort(key=lambda judge: judge[5] - judge[4], reverse=True)
    print("\n{0:18} {1:20} {2}".format("Justice", "Appointing Pres", "Yrs Served"))
    for judge in judges:
        print("{0:18} {1:20} {2}".format(judge[0] + " " + judge[1], judge[2].split(" ")[-1], judge[5] - judge[4]))
def getJusticesByState(state):
    infile = open("Justices.txt", 'r')
    records = [line.rstrip() for line in infile if line.split(',')[3] == state]
    infile.close()
    for i in range(len(records)):
        records[i] = records[i].split(',')
        records[i][4] = int(records[i][4])
        records[i][5] = int(records[i][5])
        return records
def fixCurrentJudges(judges):
    for judge in judges:
        if judge[5] == 0:
            judge[5] = 2015
main()