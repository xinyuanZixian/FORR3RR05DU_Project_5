class Node: 
    def __init__(self, d):
        self.data = d
        self.prv = None
        self.nxt = None

    def append(self,d):
        if self.nxt:
            return self.nxt.append(d)
        else:
            curr = Node(d)
            self.nxt = curr
            curr.prv = self
            return True

    def printList(self):
        return
    
    def find(self, d):
        return
    
    def delete(self, d):
        return
    
class DLL:
    def __init__(self):
        self.head = None

    def push(self,d):
        return

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
            self.head = self.head.nxt
            self.head.prv.nxt = None
            self.head.prv = None
            return True
        else:
            return self.head.delete(d)

dbl = DLL()
dbl.append(5)           # 5
dbl.append(7)           # 5 7         
#dbl.push(1)             # 1 5 7 
#dbl.push(0)             # 0 1 5 7 
#dbl.append(10)          # 0 1 5 7 10
#dbl.printList()         
#print()
#print(dbl.delete(10))   # 0 1 5 7
#dbl.printList() 
#print(dbl.find(5))      # True
#print(dbl.find(10))     # False
