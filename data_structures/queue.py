'''
Queue implementation in python.
Note:
     If you want to know the element which is dequeued from the queue, just remove '#' from lines 23 and 25.
     
'''     

class Queue:
    def __init__(self, n):
        self.queue = []
        self.lenlim = n
    
    def enqueue(self,a):
        if len(self.queue) >= self.lenlim:
            print("Overflow")
        else:
            self.queue.append(a)
    
    def dequeue(self):
        if len(self.queue)==0:
            print("Underflow")
        else:
            #p = self.queue[0]
            self.queue.pop(0)
            #return p
    
    def display(self):
        if len(self.queue)==0:
            print("Queue is Empty")
        else:
            for i in range(len(self.queue)):
                print(self.queue[i], end = ' ')
            print()

