'''
Another Linked List Implementation in python.

Usage of linked list class and its function is given from line 36.

'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Linked_List: 
    def __init__(self):
        self.head = Node(None)

    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data):
        current = head
        temp = None
        if current == None:
            temp = Node(data)
            current = temp
            return temp
        else:
            temp1 = current
            while current.next:
               current = current.next
            current.next = Node(data)
            return temp1
           
mylist= Linked_List()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head)	  