'''
Doubly Linked List implementation using Python.
Here, Prepend function is used to insert element from the left side of this data structure.
Append function is used to insert element from the right side of this data structure.

'''


class Node:
    def __init__(self, data = None):
        self.data = data
        self.prev = None
        self.next = None

class doubly_linked_list:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            new_node.prev = None
            self.head = new_node
        else:
            cur_node = self.head
            while cur_node.next:
                cur_node = cur_node.next
            cur_node.next = new_node
            new_node.prev = cur_node
            new_node.next = None
                


    def prepend(self, data):
        new_node = Node(data)
        if self.head == None:
            new_node.prev = None
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None

    
    def length(self):
        cur = self.head
        total = 0
        if self.head == None:
            return total
    
        while cur.next!=None:
            total+=1
            cur = cur.next
        return total+1

    
    def get(self, index):
        if index >= self.length():
            print("ERROR:'Get' index out of range ")
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                return cur_node.data
            cur_idx += 1

    def erase(self, index):
        if index >= self.length():
            print("ERROR : 'Erase' index out of range")
            return None  
        cur_idx = 0
        cur_node = self.head
        if index == 0:
            cur_node.next.prev = None
            self.head = cur_node.next
            return
        else:
            while True:
                last_node = cur_node.prev
                cur_node = cur_node.next
                if cur_idx == index:
                    if cur_idx == self.length()-1:
                        last_node.next = None
                        return
                    else:
                        last_node.next = cur_node
                        cur_node.prev = last_node
                        return
                cur_idx += 1



    def display(self):
        elems =[]
        cur_node = self.head
        while cur_node:
            elems.append(cur_node.data)
            cur_node = cur_node.next
        print(elems)
