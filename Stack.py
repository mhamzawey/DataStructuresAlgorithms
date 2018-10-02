class Stack:
    def __init__(self):
        self.stack = []

    def push(self,val):
        self.stack.append(val)
        return val

    def pop(self):
        return self.stack.pop(len(self.stack)-1)

    def peek(self):
        return self.stack[len(self.stack)-1]



stack = Stack()

print(stack.push(5))
print(stack.push(7))
print(stack.push(8))
print(stack.push(9))

print("peek" + str(stack.peek()))

print (stack.pop())
print (stack.pop())
print (stack.pop())
print (stack.pop())