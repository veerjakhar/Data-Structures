class Queue:
    def __init__(self, size):
        self.queue = [None] * size
        self.front = 0
        self.rear = 0
        self.size = size
        self.avalible = size

    def enqueue(self, k):
        if self.avalible == 0:
            print("Queue has been overflowed")
        else:
            self.queue[self.rear] = k
            self.rear = (self.rear + 1) % self.size
            self.avalible -= 1
    
    def nrint(self):
        print(self.queue)

    def dequeue(self):
        if self.avalible == self.size:
            print("Queue has been underflowed")
        else:

            self.queue[self.front] = None
            self.front = (self.front + 1) % self.size
            self.avalible +=  1

    def getrear(self):
        if len(self.queue) == 0:
            print("The Queue is EMPTY")
            return
        else:
            print(self.queue[-1])
            return self.queue[self.rear]

s1 = Queue(3)
s1.enqueue(9)
s1.enqueue(6)
s1.enqueue(3)
s1.enqueue(5)
s1.nrint()

s1.dequeue()
s1.dequeue()
s1.nrint()

s1.getrear()