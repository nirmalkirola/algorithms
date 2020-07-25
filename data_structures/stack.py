'''
Stack implementation in python.
Note:
     If you want to know the element which is popped from the queue, just remove '#' from lines 23 and 25.
     
'''     


class Stack:
    def __init__(self, n):
        self.stack = []
        self.lenlim = n
    
    def PushElement(self,a):
        if len(self.stack) >= self.lenlim:
            print("Overflow")
        else:
            self.stack.append(a)
    
    def PopElement(self):
        if len(self.stack)==0:
            print("Underflow")
        else:
            #p = self.stack[-1]
            self.stack.pop(-1)
            #return p
    def GetTopElement(self):
        index = len(self.stack)-1
        if index < 0:
            print("Stack is Empty")
        else:
            print(index)
            print(self.stack[index])
    
    def display(self):
        if len(self.stack)==0:
            print("Stack is Empty")
        else:
            for i in range(len(self.stack)):
                print(self.stack[i], end = ' ')
            print("Top element is : ",self.stack[len(self.stack)-1])