class Stack:
    def __init__(self):
        self.internalArray = []
    def push(self, internalArray):
        self.internalArray.append(internalArray)
    def pop(self):
        if len(self.internalArray) == 0:
            print("stack is empty")
        else:
            lastitem = self.internalArray[-1]
            del self.internalArray[-1]
            return lastitem
    def peek(self):

        if len(self.internalArray) == 0:
            print("stack is empty")
        else:
           return self.internalArray[-1]
    def __str__(self):
        return self.internalArray.__str__()

stack1 = Stack()
stack1.push(1)
stack1.push(4)
stack1.push(9)
print(stack1)
print("------------")  
popped = stack1.pop()
print(popped)
popped = stack1.pop()
print(popped)
popped = stack1.pop()
print(popped)
popped = stack1.pop()
if popped is not None:
   print(popped)
print("------------")
stack2 = Stack()
stack2.push("Linux")
stack2.push("windows")
stack2.push("mac os x")
print(stack2)
print(stack2.peek())