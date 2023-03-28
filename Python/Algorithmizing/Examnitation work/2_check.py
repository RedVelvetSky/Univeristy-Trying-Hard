class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        new_node = Node(val)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if val < current.val:
                    if current.left is None:
                        current.left = new_node
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = new_node
                        break
                    else:
                        current = current.right

flag_print = False
flag_continue = True

list_subtree = []


def pod_strom(koren: Node, x):
    global flag_print, flag_continue
    
    if koren and flag_continue:
        if koren.val == x:
            flag_print = True
            pod_strom(koren.left, x)
            pod_strom(koren.right, x)
            flag_print = False
            flag_continue = False

        pod_strom(koren.left, x)

        if flag_print:
            list_subtree.append(koren.val)

        pod_strom(koren.right, x)

bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(1)
bst.insert(4)
bst.insert(9)
bst.insert(2)

pod_strom(bst, 7)
print(list_subtree)




