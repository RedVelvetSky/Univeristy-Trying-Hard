# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None

# class BinarySearchTree:
#     def __init__(self):
#         self.root = None

#     def insert(self, val):
#         new_node = Node(val)
#         if self.root is None:
#             self.root = new_node
#         else:
#             current = self.root
#             while True:
#                 if val < current.val:
#                     if current.left is None:
#                         current.left = new_node
#                         break
#                     else:
#                         current = current.left
#                 else:
#                     if current.right is None:
#                         current.right = new_node
#                         break
#                     else:
#                         current = current.right

#     def search(self, val):
#         current = self.root
#         while current is not None:
#             if val == current.val:
#                 # self.dfs(current)
#                 print("da")
#             elif val < current.val:
#                 current = current.left
#             else:
#                 current = current.right
#         return False

#     def print_tree(self) -> None:
#         if self.root is not None:
#             self._print_tree_(self.root)

#     def _print_tree_(self, current: Node) -> None:
#         if current is not None:
#             self._print_tree_(current.left)
#             print(current.val)
#             self._print_tree_(current.right)

#     def bfs(self):
#         if self.root is None:
#             return None

#         queue = []
#         queue.append(self.root)

#         while len(queue) > 0:
#             current = queue.pop(0)
#             print(current.val)
#             if current.left is not None:
#                 queue.append(current.left)
#             if current.right is not None:
#                 queue.append(current.right)

#     def dfs(self, current) -> None:
#         # if current is not None:
#         #     self._pre_order_(current)
#         self._pre_order_(current)
            
#     def _pre_order_(self, current: Node) -> None:
#         if current is not None:
#             print(current.val)
#             self._pre_order_(current.left)
#             self._pre_order_(current.right)

# bst = BinarySearchTree()
# bst.insert(5)
# bst.insert(3)
# bst.insert(7)
# bst.insert(1)
# bst.insert(4)
# bst.insert(9)
# bst.insert(2)
# bst.search(2)
# # bst.print_tree()
# # print("---------")
# # bst.bfs()
# # print("---------")
# # bst.dfs()

# # from collections import deque
# # def last_level_leaves(root):
# #     if not root:
# #         return []
# #     output = []
# #     max_level = 0
# #     queue = deque()
# #     queue.append((root, 0))
# #     while queue:
# #         current, level = queue.popleft()
# #         if not current.left and not current.right:
# #             if level == max_level:
# #                 output.append(current.val)
# #             elif level > max_level:
# #                 max_level = level
# #                 output = [current.val]
# #         if current.left:
# #             queue.append((current.left, level+1))
# #         if current.right:
# #             queue.append((current.right, level+1))
# #     return output

# # print(last_level_leaves(bst.root))



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

    def search(self, val):
        current = self.root
        while current is not None:
            if val == current.val:
                self.dfs(current, val)
                break
            elif val < current.val:
                current = current.left
            else:
                current = current.right
        return False

    def print_tree(self) -> None:
        if self.root is not None:
            self._print_tree_(self.root)

    def _print_tree_(self, current: Node) -> None:
        if current is not None:
            self._print_tree_(current.left)
            print(current.val)
            self._print_tree_(current.right)

    def bfs(self):
        if self.root is None:
            return None

        queue = []
        queue.append(self.root)

        while len(queue) > 0:
            current = queue.pop(0)
            print(current.val)
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)

    def dfs(self, curr, val) -> None:
        self._pre_order_(curr, val)
            
            
    def _pre_order_(self, current: Node, val):
        sub = []
        if current is not None:
            sub.append(current.val)
            if val in sub:
                sub.pop(0)
            self._pre_order_(current.left, val)
            self._pre_order_(current.right, val)
        return sub

bst = BinarySearchTree()

bst.insert(2)
bst.insert(25)
bst.insert(9)
bst.insert(80)
bst.insert(0)
bst.insert(5)
bst.insert(15)
bst.insert(8)

print(bst.search(25))

# bst.insert(5)
# bst.insert(3)
# bst.insert(7)
# bst.insert(1)
# bst.insert(4)
# bst.insert(9)
# bst.insert(2)
# bst.search(3)
# bst.print_tree()
# print("---------")
# bst.bfs()
# print("---------")
# bst.dfs()

# from collections import deque
# def last_level_leaves(root):
#     if not root:
#         return []
#     output = []
#     max_level = 0
#     queue = deque()
#     queue.append((root, 0))
#     while queue:
#         current, level = queue.popleft()
#         if not current.left and not current.right:
#             if level == max_level:
#                 output.append(current.val)
#             elif level > max_level:
#                 max_level = level
#                 output = [current.val]
#         if current.left:
#             queue.append((current.left, level+1))
#         if current.right:
#             queue.append((current.right, level+1))
#     return output

# print(last_level_leaves(bst.root))