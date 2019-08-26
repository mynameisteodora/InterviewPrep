def BinaryTree(r):
    return [r, [], []]


def insertLeft(root, newBranch):
    # pop the list representing the left child
    t = root.pop(1)

    if len(t) > 1:
        # There is already an element there
        # We need to push it down the tree
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])

    return root


def insertRight(root, newBranch):
    t = root.pop(2)

    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])


def getRootVal(root):
    return root[0]


def setRootVal(root, newVal):
    root[0] = newVal


def getLeftChild(root):
    return root[1]


def getRightChild(root):
    return root[2]


if __name__ == '__main__':
    # b - a - c - d - e
    x = BinaryTree('a')
    insertLeft(x, 'b')
    insertRight(x, 'c')
    insertRight(getRightChild(x), 'd')
    insertLeft(getRightChild(getRightChild(x)), 'e')
    print(getLeftChild(x))

    y = BinaryTree('a')
    insertLeft(y, 'b')
    insertRight(y, 'c')
    insertRight(getLeftChild(x), 'd')
    insertLeft(getRightChild(x), 'e')
    insertRight(getRightChild(x), 'f')
    print(getLeftChild(y))
