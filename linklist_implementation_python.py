#implementing linked list in python

class node:
    def __init__(self, x):
        self.val = x
        self.next = None
    

class linkedlist:

    def __init__(self, n):
        self.head = n
    
    def __init__(self):
        self.head = None
        
    def add(self, i):
        n = node(i)
        if(self.head == None):
            self.head = n
            return
        temp = self.head
        while(temp.next != None):
            temp = temp.next
        temp.next = n
    
    def printLinklist(self):
        temp = self.head
        while(temp != None):
            print temp.val
            temp = temp.next
            
    def reverse(self):
        tail = self.head
        if tail.next == None:
            return
        while tail.next.next != None:
            nnode = tail.next
            nnnode = tail.next.next
            tail.next = nnnode
            nnode.next = self.head
            self.head = nnode
        temp = tail.next
        temp.next = self.head
        self.head = temp
        tail.next = None
            
l = linkedlist()
l.add(3)
l.add(4)
l.add(2)
l.add(1)
l.add(5)
l.printLinklist()