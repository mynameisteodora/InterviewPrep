class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def set_next(self, node):
        next_node = Node(node)
        self.next = next_node
        return next_node

    def __str__(self):
        return str(self.value)

if __name__ == '__main__':
    # list 1
    n1 = Node(5)
    n2 = n1.set_next(7)
    n3 = n2.set_next(0)
    n4 = n3.set_next(4)

    # list 2
    n5 = Node(10)
    n6 = n5.set_next(2)
    n7 = n6.set_next(1)

    print("List 1:")
    n = n1
    while n is not None:
        print(n)
        n = n.next
        print("new n = {}".format(n))





