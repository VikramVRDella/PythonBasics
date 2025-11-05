class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def push(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        print(f"Element Pushed: {value}")

    def pop(self):
        if self.is_empty():
            print("Stack is Empty, cannot pop")
            return
        popped_value = self.head.value
        self.head = self.head.next
        print(f"Popped Data: {popped_value} from Stack")
        return popped_value

    def peek(self):
        if self.is_empty():
            print("Stack is Empty..")
            return None
        return self.head.value

    def display(self):
        if self.is_empty():
            print("Stack is Empty...")
            return
        current = self.head
        print("Stack elements:")
        while current:
            print(current.value)
            current = current.next

# Testing the stack
mystack = Stack()
mystack.push('A')
mystack.push('B')
mystack.push('C')

mystack.display()
print("Top element:", mystack.peek())
mystack.pop()
mystack.display()
