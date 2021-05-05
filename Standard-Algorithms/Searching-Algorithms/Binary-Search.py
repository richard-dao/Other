# Python

# While-Loop
def binarySearch(value, sList):
    low, high = 0, len(sList)-1
    while (low <= high):
        mid = int((low+high)/2)
        if (sList[mid] == value):
            return mid
        elif(value < sList[mid]):
            high = mid - 1
        elif (value > sList[mid]):
            low = low + 1
    return -1

# For-Loop
def binarySearchFor(value, sList):
    low, high = 0, len(sList)-1
    for x in range(0, len(sList)):
        if (low > high):
            break
        mid = int((low+high)/2)
        if (value == sList[mid]):
            return mid
        if (value < sList[mid]):
            high = mid - 1
        elif (value > sList[mid]):
            low = low + 1
    return -1

# Recursive
def binarySearchRecursive(sList, low, high, value):
    mid = int((low+high)/2)
    if (low > high):
        return -1
    if (sList[mid] == value):
        return mid
    if (value < sList[mid]):
        high = high - 1
    elif(value > sList[mid]):
        low = low + 1
    return binarySearchRecursive(sList, low, high, value)
