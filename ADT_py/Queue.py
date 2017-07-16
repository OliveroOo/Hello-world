#-*-coding utf-8 -*-

'''
2017/7/15
Author:Zihyan
Queue
'''

class Queue:
    def __init__(self):
        self.length = 0
        self.head = None

    def is_empty(self):
        return (self.length == 0)

    def insert(self, cargo):
        node = Node(cargo)
        node.next = None
        if self.head == None:
            # if list is empty the new node goes first
            self.head = node
        else:
            # find the last node in the list
            last = self.head
            while last.next:
                last = last.next
            # append the new node
            last.next = node
        self.length = self.length + 1

    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length = self.length - 1 
        return cargo

class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo 
        self.next = next

    def __str__(self):
        return str(self.cargo)

    def print_backward(self):
        if self.next != None:
            tail = self.next
            tail.print_backward()
        return tail.cargo

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
   
    def print_backward(self):
        print("[")
        if self.head != None:
            self.head.print_backward()
        print("]")

    def addFirst(self, cargo):
        node = Node(cargo)
        node.next = self.head
        self.head = node
        self.length = self.length + 1


class ImprovedQueue:
    def __init__(self):
        self.head = None
        self.last = None 
        self.length = 0
    
    def is_empty(self):
        return (self.length == 0)

    def insert(self, cargo):
        node = Node(cargo)
        node.next = None 
        if self.length == 0:
            self.head = self.last = node
        else:
            #find the last 
            last = self.last
            last.next = node
            self.last = node
        self.length = self.length + 1
    
    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length = self.length - 1
        if self.length == 0:
            self.last = None
        return cargo
        
class PriorityQueue:
    def __init__(self):
        self.item = []
    
    def insert(self, cargo):
        self.item.append(cargo)
   
    def is_empty(self):
        return (self.item == [])

    def remove(self):
        maxi = 0
        for i in range(1,len(self.item)):
            if self.item[i] > self.item[maxi]:
                maxi = i
        item = self.item[maxi]
        self.item[maxi:maxi+1] = []
        return item
        
if __name__ == '__main__':
    import timeit
    start = timeit.default_timer()
    q = PriorityQueue()
    for i in range(100):
        q.insert(i)
    while not q.is_empty():
        print(q.remove())       
    stop = timeit.default_timer()
    print("Run time:",  stop - start)
