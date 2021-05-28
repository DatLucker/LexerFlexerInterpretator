class Elem:
    def __init__ (self, val = None):
        self.value = val
        self.nextelem = None

class LinkedList:
    def __init__(self , *elems):
        self.head = None
        for elem in elems[0]:
            self.push(elem)

    def __repr__(self):
        curr = self.head
        string = '[ '
        while curr is not None:
            string += f'{curr.value},'
            curr = curr.nextlem
        string += ']'

        return string


    def contains(self, value):
        lastlem = self.head
        while (lastlem):
            if value == lastlem.value:
                return True
            else:
                lastlem = lastlem.nextlem;
        return False

    def push(self, value):
        newelem = Elem(value)
        if self.head is None:
            self.head = newelem
            return
        lastlem = self.head
        while (lastlem.nextelem):
            lastlem = lastlem.nextelem
        lastlem.nextelem = newelem

    def get(self, index):
        lastlem = self.head
        elemIndex = 0
        while elemIndex <= index:
            if elemIndex == index:
                return lastlem.value
            elemIndex = elemIndex + 1
            lastlem = lastlem.nextlem

    def remove(self, value):
        curr = self.head
        if curr is not None:
            if curr.value == value:
                self.head = curr.nextlem
                return
        while curr is not None:
            if curr.value == value:
                break
            last = curr
            curr = curr.nextelem
        if curr == None:
            return
        last.nextlem = curr.nextelem

    def printList(self):
        current = self.head
        while current is not None:
            print(current.value,end=' ')
            current = current.nextlem