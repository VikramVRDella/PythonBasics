class Stack:
    def __init__(self):
        self.stack=[]
    
    def push(self,element):
        self.stack.append(element)
        print("Element Pushed...")
    
    def pop(self,element):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            self.stack.pop(element)
    def peek(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            return self.stack[-1]
    def display(self):
        print(self.stack)

mystack= Stack()

mystack.push('A')
mystack.push('B')
mystack.push('C')

mystack.display()


