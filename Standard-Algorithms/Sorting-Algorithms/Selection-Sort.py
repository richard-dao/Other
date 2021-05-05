# Python
def selectionSort(sList):
    for x in range(0, len(sList)):
        minIndex = x
        for y in range (x+1, len(sList)):
            if (sList[y] < sList[minIndex]):
                minIndex = y
        temp = sList[x]
        sList[x] = sList[minIndex]
        sList[minIndex] = temp
    return
