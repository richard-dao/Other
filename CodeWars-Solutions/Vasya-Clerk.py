# Python
def tickets(people):
    amount25 = 0
    amount50 = 0
    amount100 = 0
    change = 0
    
    for x in range (0, len(people)):
        if (people[x] == 25):
            amount25 = amount25 + 1
        if (people[x] == 50):
            amount50 = amount50 + 1
        if (people[x] == 100):
            amount100 = amount100 + 1
        
        change = people[x] - 25
        
        if (change == 25):
            if (amount25 > 0):
                amount25 = amount25 - 1
            else:
                return "NO"
        if (change == 75):
            if (amount25 > 0 and amount50 > 0):
                amount25 = amount25 - 1
                amount50 = amount50 - 1
            elif(amount25 > 2):
                amount25 = amount25 - 3
            else:
                return "NO"
    return "YES"
