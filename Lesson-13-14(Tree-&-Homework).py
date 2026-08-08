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

def preOrderTraversal(root):
    print(root.data)
    if root.leftNode != None:
        preOrderTraversal(root.leftNode)
    if root.rightNode != None:
        preOrderTraversal(root.rightNode)

def postOrderTraversal(root):
    print(root.data)
    if root.leftNode != None:
        postOrderTraversalroot(root.leftNode)
    if root.rightNode != None:
        postOrderTraversal(root.rightNode)

def count_nodes(root):
    if root == None:
        return 0
    return 1 + count_nodes(root.leftNode) + count_nodes(root.rightNode)

def biggest(root):
    if root == None:
        return -1000
    leftmax = biggest(root.leftNode)
    rightmax = biggest(root.rightNode)
    return max(root.data, leftmax, rightmax)

def tad(root):
    if root == None:
        return 0
    return root.data + tad(root.rightNode) + tad(root.leftNode)

def lookin(root, key):
    if root == None:
        return False
    if root.data == key:
        return True
    return lookin(root.leftNode, key) or lookin(root.rightNode, key)

def high(root):
    if root == None:
        return -1
    left_h = high(root.leftNode)
    right_h = high(root.rightNode)
    return 1 + max(left_h, right_h)
    
    

t = Tree(5)
t.leftNode = Tree(10)
t.rightNode = Tree(15)

t.leftNode.leftNode = Tree(40)
t.rightNode.rightNode = Tree(20)
t.rightNode.leftNode = Tree(30)
t.rightNode.rightNode.rightNode = Tree(35)
inOrderTraversal(t)
print(count_nodes(t))
print("The Maximum value in the tree is: ", biggest(t))
print("The total of the entire tree is: ", tad(t))
print("Does the value exist: ", lookin(t, 39))
print("The hight or the tree is: ", high(t))

