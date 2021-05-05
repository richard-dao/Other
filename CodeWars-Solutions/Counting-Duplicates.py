# Python
def duplicate_count(text):
    # Your code goes here
    sum = 0
    foundList = list()
    count = 0
    text = text.lower()
    for x in range (0, len(text)):
        count = 0
        for y in range (x+1, len(text)):
            if (text[x:x+1] == text[y:y+1]):
                if (text[x:x+1]) not in foundList:
                    foundList.append(text[x:x+1])
                    count = count + 1
        if (count > 0):
            sum = sum + 1
    return sum
