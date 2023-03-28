class Vertex:
    def __init__(self, val = None, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    # def insert(self, value):
    #     new_node = Vertex(value)
    #     if value:
    #         if value < self.info:
    #             if self.left is None:
    #                 self.left = new_node
    #             else:
    #                 self.left.insert(value)
    #         elif value > self.info:
    #             if self.right is None:
    #                 self.right = new_node
    #             else:
    #                 self.right.insert(value)
    #         else:
    #             self.info = value

    def insert(self, val):
        # new_node = Node(val)
        if self.root is None:
            self.root = Vertex(val)
        else:
            current = self.root
            while True:
                if val < current.val:
                    if current.left is None:
                        current.left = Vertex(val)
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = Vertex(val)
                        break
                    else:
                        current = current.right


flag_print = False
flag_continue = True

list_subtree = []


def pod_strom(koren: Vertex, x):
    global flag_print, flag_continue
    
    if koren and flag_continue:
        if koren.info == x:
            flag_print = True
            pod_strom(koren.left, x)
            pod_strom(koren.right, x)
            flag_print = False
            flag_continue = False

        pod_strom(koren.left, x)

        if flag_print:
            list_subtree.append(koren.info)

        pod_strom(koren.right, x)


root = Vertex(7)
root.insert(2)
root.insert(25)
root.insert(9)
root.insert(80)
root.insert(0)
root.insert(5)
root.insert(15)
root.insert(8)

pod_strom(root, 25)
print(list_subtree)

# Time complexity O(n), space complexity is O(h), where h - tree height
