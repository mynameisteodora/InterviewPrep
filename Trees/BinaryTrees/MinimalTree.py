"""
Minimal Tree:
Given a sorted (increasing order) array with unique integer elements,
write an algorithm to create a binary search tree with minimal height.
"""
from Trees.BinaryTrees.TreeWithNodes import BinaryTree

class MinimalTree:

    def __init__(self, lst):
        self.lst = lst

    def build_tree(self, start, end):
        if end < start:
            return None

        mid = (start + end)//2
        node = BinaryTree(self.lst[mid])
        print("Current root node = {}".format(node.getRootVal()))
        left = self.build_tree(start, mid - 1)
        right = self.build_tree(mid + 1, end)
        if left is not None:
            node.insertLeft(left)

        if right is not None:
            node.insertRight(right)

        return node

if __name__ == '__main__':

    lst = [1,4,7,10,30,34]
    minimal_tree = MinimalTree(lst)
    root = minimal_tree.build_tree(0, len(lst) - 1)
    root.traversal_preorder(root)





