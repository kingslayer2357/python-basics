class Stack(object):
    
    def __init__(self):
        self.stack=[]
    def push(self,val):
        self.stack.append(val)
    def pop(self):
        self.stack.pop()
    def dis(self):
        print(self.stack)
s=Stack()
s.push(2)
s.push(3)
s.push(300)
s.push(90)
s.pop()
s.pop()
s.dis()
