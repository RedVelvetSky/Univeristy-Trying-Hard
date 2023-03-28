class VertexBinTree:
    """class for representing the top of a binary tree""" 
    def __init__(self, info = None, left = None, right = None):
        self.info = info # vertex number
        self.left = left # left child 
        self.right = right # right child

def level(root : VertexBinTree):
    """
    root : root of the specified binary tree
    returns : the number of the level at which the maximum value is stored
    """
    if not root:
        return -1
    max_value = root.info
    max_level = 0
    level = 0
    queue = [(root, level)]
    while queue:
        current, current_level = queue.pop(0)
        if current.info > max_value:
            max_value = current.info
            max_level = current_level
        if current.left:
            queue.append((current.left, current_level+1))
        if current.right:
            queue.append((current.right, current_level+1))
    return max_level


root = VertexBinTree(7)
root.left = VertexBinTree(2)
root.right = VertexBinTree(25)
root.right.left = VertexBinTree(9)
root.right.right = VertexBinTree(80)
root.left.left = VertexBinTree(0)
root.left.right = VertexBinTree(5)
root.right.left.left = VertexBinTree(15)
root.right.left.right = VertexBinTree(8)

result = level(root)
print("The level with the maximum value is:", result)
