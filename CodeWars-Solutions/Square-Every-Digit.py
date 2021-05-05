# Python
def square_digits(num):
    y = num
    leng = len(str(num))
    squareDigits = list() # int
    stringSquares = [] # strings
    rString = ""
    for x in range (0, leng):
      squareDigits.append("10")
    for x in range (leng-1, -1, -1):
        squareDigits[x] = ((y % 10) * (y % 10))
        y = int(y/10)
        print(y)
    for x in range (0, leng):
        stringSquares.append(str(squareDigits[x]))
    for x in range(0, len(stringSquares)):
        rString += stringSquares[x]
    return int(rString)
    
print(square_digits(4149))
