class Node:
    def __init__(self, data, left=None, right=None):
      self.data = data
      self.left = left
      self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self, node, data):
      if node == None:
        return Node(data)
      if data == node.data:
        return node
      if data < node.data:
        node.left = self.insert(node.left, data)
      else:
        node.right = self.insert(node.right, data)
      return node
    

def callback(value):
  print(value, end=' ')

def preorder(node, callback):
  if(node != None):
    callback(node.data)
    preorder(node.left, callback)
    preorder(node.right, callback)
def inorder(node, callback):
  if(node != None):
    inorder(node.left, callback)
    callback(node.data)
    inorder(node.right, callback)
def postorder(node, callback):
  if(node != None):
    postorder(node.left, callback)
    postorder(node.right, callback)
    callback(node.data)

def binary_search(node, value):
  if(node != None):
    if(node.data == value):
      print("Found", value)
    binary_search(node.left, value)
    binary_search(node.right, value)

data = [10,11,4,2,3,7,1,3,5,6]
bst = BinarySearchTree()
for i in data:
  bst.root = bst.insert(bst.root, i)

binary_search(bst.root, 5)