class Stack:
    def __init__(self):
        self.stack = []

    def push(self, k):
        self.stack.append(k)
        
    def display(self):
        print(self.stack)
    
    def size(self):
        return len(self.stack)

    def pop(self):
        if len(self.stack) == 0:
            print("Stack 1(List 1) is empty")
        else:
            return self.stack.pop(-1)

x = int(input("Instert the number you want to have converted in to binary: "))
s1 = Stack()

while x > 0:
    y = x % 2
    s1.push(y)
    x = x // 2
result = ""

while s1.size() > 0:
    result = result + str(s1.pop())

print(result)