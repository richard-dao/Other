# Python
def count_bits(n):
    nBin = bin(n)
    nBin = str(nBin)
    count = 0;
    for x in range(0, len(nBin)):
        if (nBin[x:x+1] == "1"):
            count = count + 1
    return count
