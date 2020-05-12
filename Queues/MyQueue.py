class MyQueue:

    def __init__(self):
        self.length = 0
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
        self.length += 1

    def dequeue(self):
        if self.length > 0:
            item = self.items.pop(0)
            self.length -= 1
            return item
        else:
            return None

    def peek(self):
        return self.items[0]

    def is_empty(self):
        return self.length == 0

    def __str__(self):
        return str(self.items)

    def size(self):
        return self.length

if __name__ == '__main__':
    q = MyQueue()
    q.enqueue(5)
    q.enqueue(10)
    q.enqueue(140)
    print(q)
    q.dequeue()
    print(q)

