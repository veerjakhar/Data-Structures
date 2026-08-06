class Tree:
    def __init__(self, data):
        self.data = data
        self.leftNode = None
        self.rightNode = None

def inOrderTraversal(root):
    if root.leftNode != None:
        inOrderTraversal(root.leftNode)
    print(root.data)
    if root.rightNode != None:
        inOrderTraversal(root.rightNode)
    print(root.data)

t = Tree(5)
t.leftNode = Tree(4)
t.rightNode = Tree(6)
inOrderTraversal(t)