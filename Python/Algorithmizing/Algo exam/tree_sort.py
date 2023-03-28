test_vector = [170, 45, 75, 90, 802, 24, 2, 66]

class Node:
    def __init__(self, key = 0) -> None:
        self.key = key
        self.left = None
        self.right = None

root = Node()
root = None

def insert(key):
    global root
    root = insert_recursive(root, key)

def insert_recursive(root, key):
    if root == None:
        root = Node(key)
        return root
    if key < root.key:
        root.left = insert_recursive(root.left, key)
    if key > root.key:
        root.right = insert_recursive(root.right, key)
    return root

def inorder_BST_recursive(root):
    if root != None:
        inorder_BST_recursive(root.left)
        print(root.key, end = " ")
        inorder_BST_recursive(root.right) 

def tree_insert (arr):
    for i in range (len(arr)):
        insert(arr[i])

tree_insert (test_vector)
inorder_BST_recursive (root)