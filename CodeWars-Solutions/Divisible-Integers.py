# Python
def get_count(n):
    # your code
    count = 0
    strN = str(n)
    subIntList = list()
    subIntConvert = list()
        
# Variables
    for x in range (0, len(strN)):
        for y in range (x, len(strN)+1):
            subIntList.append(strN[x:y])
# Should fill list with every possible sub-integer
# Let's test it | First test seems to show that its missing "30", also giving weird blanks
    y = 0
    for x in range (0, len(subIntList)):
        if (subIntList[y] == ""):
            subIntList.pop(y)
            y = y -1;
        y = y + 1;
    for x in range (0, len(subIntList)):
        subIntConvert.append(int(subIntList[x]))

    for x in range (0, len(subIntConvert)):
        if (subIntConvert[x] != 0 and subIntConvert[x] != n):
            if (n % subIntConvert[x] == 0):
                count = count + 1
    return count
