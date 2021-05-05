# Python
def get_sum(a,b):
    #good luck!
    sum = 0
    if (a == b):
        return a
    if (a < b):
        sum = a
        for x in range (a, b):
            sum += (x + 1)
        return sum
    if (b < a):
        sum = b
        for x in range (b, a):
            sum += (x + 1)
        return sum
