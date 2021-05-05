# Python
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def append(listA, listB):
    # Your code goes here.
    # Remember to return the head of the list.
    if (listA == None and listB == None):
        return None
    if (listA == None):
        return listB
    if (listB == None):
        return listA
    
    current = listA
    while (current.next != None):
        current = current.next
    current.next = listB
    return listA
