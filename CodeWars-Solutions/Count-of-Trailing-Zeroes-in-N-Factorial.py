# Python
def zeros(n):
    sum = 0
    x = 5
    while (n / x >= 1):
        sum = sum + int(n/x)
        x = x * 5
    return sum
