#Stack Implementation  
class Stack:
    def __init__(self):
         self.s=[]
        
    def push(self,element):
        self.s.append(element)
        
    def concate(self,itemsList):
        self.s += itemsList
        
    def pop(self):
        self.s.pop() 
    
    def print(self):
        print(self.s)
    
    def index(self,ind):
        print(self.s[ind])
        
    def is_empty(self):
        print(self.s==[])
        
    def peek(self):
        print(self.s[-1])
        
stack1 = Stack()
stack1.push(1)
stack1.push(2)
stack1.push(3)
stack1.push(4)
stack1.push(5)
stack1.print()
stack1.concate([6,7,8,9])
stack1.pop()
stack1.print()
stack1.index(4)
stack1.is_empty()
stack1.peek()