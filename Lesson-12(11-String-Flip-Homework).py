class Stack:
    def __init__(self):
        self.stack = []

    def push(self, k):
        self.stack.append(k)

    def pop(self):
        if len(self.stack) == 0:
            print("The list is empty, Please submit a value")
            return
        else:
            return self.stack.pop()

    def ismt(self):
        return len(self.stack) == 0



s1 = Stack()

value = input("Enter A String: ")

for i in value:
    s1.push(i)

rstring = ""

while not s1.ismt():
    rstring += s1.pop()

print("The revese string is : ", rstring)

