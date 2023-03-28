class VertexBinTree:
    def __init__(self, info = None, levy = None, pravy = None):
        self.info = info      # číslo vrcholu
        self.levy = levy      # levé dítě 
        self.pravy = pravy    # pravé dítě

class BinaryTree:
    def __init__(self):
        self.root = None

    def search(self, info):
        current = self.root
        while current is not None:
            if info == current.info:
                return True
            elif info < current.info:
                current = current.levy
            else:
                current = current.pravy
        return False

    def insert(self, info):
        new_node = VertexBinTree(info)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if info < current.info:
                    if current.levy is None:
                        current.levy = new_node
                        break
                    else:
                        current = current.levy
                else:
                    if current.pravy is None:
                        current.pravy = new_node
                        break
                    else:
                        current = current.pravy

    def dfs(self, srch) -> None:
        if self.root is not None:
            self._pre_order_(self.root, srch)
            
    def _pre_order_(self, current: VertexBinTree, srch) -> None:
        if current is not None:
            if current == srch:
                print(current.info)
            self._pre_order_(current.levy, srch)
            self._pre_order_(current.pravy, srch)

def subtree(root : VertexBinTree, x : int):
    if root is None:
        return []
    elif root.info == x:
        return [root.info] + subtree(root.levy, x) + subtree(root.pravy, x)
    else:
        return subtree(root.levy, x) + subtree(root.pravy, x)


bst = BinaryTree()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(1)
bst.insert(4)
bst.insert(9)
bst.insert(2)
bst.dfs(3)
# subtree(bst.5, 3)

root = TopBinTree(5, TopBinTree(3, TopBinTree(2), TopBinTree(4)), TopBinTree(7, TopBinTree(6), TopBinTree(8)))
x = 5
result = subtree(root, x)
print(result) # prints [5, 3, 2, 4, 7, 6]