class Stack:
    def __init__(self):
        self.mainstack = []
        self.minstack = []

    def push(self, k):
        self.mainstack.append(k)
        if len(self.minstack) == 0 or k <= self.minstack[-1]:
            self.minstack.append(k)

    def pop(self):
        if len(self.mainstack) == 0:
            print("The main list is empty")
        
        remove = self.mainstack.pop()
        if remove == self.minstack[-1]:
            self.minstack.pop()
        return remove

    def top(self):
        if len(self.mainstack) == 0:
            print("The main list is empty")
            return
        else:
            return self.mainstack[-1]

    def above(self):
        if len(self.minstack) == 0:
            print("The list you are trying to reach is empty")
            return
        else:
            return self.minstack[-1]

    def display(self):
        if len(self.mainstack) and len(self.minstack) == 0:
            print("Both the lists are empty")
            return

        elif len(self.mainstack) == 0:
            print("The main list is empty")
            return

        elif len(self.mainstack) == 0:
            print("The second list is empty")
            return

        else:
            print(self.mainstack)
            print(self.minstack)

s1 = Stack()
s1.push(10)
s1.push(9)
s1.push(5)
s1.push(3)
s1.push(7)
s1.push(7)
s1.push(8)
s1.push(1)
s1.display()

print(s1.above())

s1.pop()
s1.pop()

s1.display()
print(s1.above())
