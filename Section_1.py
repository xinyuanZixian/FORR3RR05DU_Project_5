class Node:
    def __init__(self, d):
        self.data = d
        self.prv = None
        self.nxt = None

    def append(self, d):
        if self.nxt:
            return self.nxt.append(d)
        else:
            curr = Node(d)
            self.nxt = curr
            curr.prv = self
            return True

    def printList(self):
        if self.nxt:
            print(self.data, end = ", ")
            return self.nxt.printList()
        else:
            print(self.data)

    def find(self, d):
        if self.data == d:
            return True
        elif  self.data != d and self.nxt != None:
            return self.nxt.find(d)
        else:
            return False

    def delete(self, d):
        if self.data == d:
            if self.nxt:
                self.prv.nxt = self.nxt
                self.nxt.prv = self.prv
                self = None
                return True
            else:
                self.prv.nxt = None
                self = None
                return True
        elif self.data != d and self.nxt != None:
            return self.nxt.delete(d)
        else:
            return False


class DLL:
    def __init__(self):
        self.head = None

    def push(self, d):
        if self.head:
            curr = Node(d)
            self.head.prv = curr
            curr.nxt = self.head
            curr.prv = None
            self.head = curr
            return True
        else:
            self.head = Node(d)
            return True
    def append(self, d):
        if self.head:
            return self.head.append(d)
        else:
            self.head = Node(d)
            return True

    def printList(self):
        if self.head:
            self.head.printList()
        else:
            print("Empty list!")

    def find(self, d):
        if self.head:
            return self.head.find(d)
        else:
            return False
        
    def delete(self, d):
        if self.head is None:
            return -1
        elif self.head.data == d:
            if self.head.nxt:
                self.head = self.head.nxt
                self.head.prv.nxt = None
                self.head.prv = None
                return True
            else:
                self.head = None
                return True
        else:
            return self.head.delete(d)

dbl = DLL()
dbl.append(5)
dbl.append(7)
dbl.push(1)
dbl.push(0)
dbl.append(10)
dbl.printList()
print()
print(dbl.delete(10))
dbl.printList()
print(dbl.find(5))
print(dbl.find(10))
