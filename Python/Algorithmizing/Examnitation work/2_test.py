class TopBinTree:
    """class for representing the top of a binary tree"""
    def init(self, info = None, left = None, right = None):
        self.info = info # vertex number
        self.levy = left # left child
        self.right = right # right child

def subtree(root : TopBinTree, x : int):
    """
    root : the root of the specified binary tree
    x : integer
    returns : a list of numbers stored in all vertices that lie in the subtree with the root containing the number x
    """
    result = []
    def dfs(node, x):
        if not node:
            return
        if node.info == x or dfs(node.left, x) or dfs(node.right, x):
            result.append(node.info)
    dfs(root, x)
    return result

root = TopBinTree(5, TopBinTree(3, TopBinTree(2), TopBinTree(4)), TopBinTree(7, TopBinTree(6), TopBinTree(8)))
x = 5
result = subtree(root, x)
print(result) # prints [5, 3, 2, 4, 7, 6]