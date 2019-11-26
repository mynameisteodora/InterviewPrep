from queue import Queue

class BinaryTree:

    bfs_queue = Queue()

    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def traversal_preorder(self, tree):
        if tree:
            print(tree.getRootVal())
            self.traversal_preorder(tree.getLeftChild())
            self.traversal_preorder(tree.getRightChild())

    def traversal_inorder(self, tree):
        if tree:
            self.traversal_inorder(tree.getLeftChild())
            print(tree.getRootVal())
            self.traversal_inorder(tree.getRightChild())

    def traversal_postorder(self, tree):
        if tree:
            self.traversal_postorder(tree.getLeftChild())
            self.traversal_postorder(tree.getRightChild())
            print(tree.getRootVal())

    def height(self, tree):
        if tree is None:
            return 0

        return 1 + max(self.height(tree.getLeftChild()), self.height(tree.getRightChild()))

    def diameter(self, tree):
        if tree is None:
            return 0

        lheight = self.height(tree.getLeftChild())
        rheight = self.height(tree.getRightChild())

        ldiameter = self.diameter(tree.getLeftChild())
        rdiameter = self.diameter(tree.getRightChild())

        # Return max of the following tree:
        # 1) Diameter of left subtree
        # 2) Diameter of right subtree
        # 3) Height of left subtree + height of right subtree +1
        return max(lheight + rheight + 1, max(ldiameter, rdiameter))

    def breadth_first_traversal(self, tree):
        q = Queue()
        q.put(tree)

        while(not q.empty()):
            e = q.get()
            print(e.getRootVal())
            if(e.leftChild != None):
                q.put(e.leftChild)
            if(e.rightChild != None):
                q.put(e.rightChild)


if __name__ == '__main__':
    tree = BinaryTree('9')
    tree.insertLeft('1')
    tree.insertRight('u')
    b1 = tree.getLeftChild()
    b1.insertLeft('h')
    b1.insertRight('n')
    h = b1.getLeftChild()
    h.insertLeft('c')
    h.insertRight('t')
    c = h.getLeftChild()
    c.insertRight('e')
    t = h.getRightChild()
    t.insertLeft('1')

    u = tree.getRightChild()
    u.insertLeft('/')
    u.insertRight('d')

    backsh = u.getLeftChild()
    backsh.insertLeft('o')
    backsh.insertRight('.')

    o = backsh.getLeftChild()
    o.insertLeft('o')
    o.insertRight('f')

    d = u.getRightChild()
    d.insertLeft('n')
    d.insertRight('i')

    i2 = d.getRightChild()
    i2.insertRight('f')

    print("Postorder traversal")
    tree.traversal_postorder(tree)

    # print("The rightmost node is: ", tree.getRightChild().getRightChild().getRootVal())
    #
    print("Preorder traversal:")
    tree.traversal_preorder(tree)
    #
    print("Inorder traversal:")
    tree.traversal_inorder(tree)
    #
    # print("Height of tree:")
    # print(tree.height(tree))
    #
    # print("Diameter of tree:")
    # print(tree.diameter(tree))
    #
    # print("BF traversal")
    # tree.breadth_first_traversal(tree)