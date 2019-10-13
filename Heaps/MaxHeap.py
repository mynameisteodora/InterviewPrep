'''
You have been given a sequence A of N digits. Each digit in this sequence ranges from 1 to  .
You need to perform 2 types of operations on this list:

: Add element x to the end of the list.
: Find the maximum element in the current sequence.
For each query of type 2, you need to print the result of that operation.

Input Format

The first line consist of a single integer N denoting the size of the initial sequence.
The next line consists of N space separated integers denoting the elements of the initial sequence.
The next line contains a single integer q denoting the number of queries. The next q lines contains the details of the operation.
The first integer type indicates the type of query.
If typei ==1, it is followed by another integer x and you need to perform operation of type 1 else operations of type 2

Output Format

For each operation of the second type, print a single integer on a new line.
'''


# class for handling a maxheap
class MaxHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] > self.heapList[i // 2]:
                self.heapList[i], self.heapList[i // 2] = self.heapList[i // 2], self.heapList[i]

            i = i // 2

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize += 1
        self.percUp(self.currentSize)

    def percDown(self, i):
        while i * 2 < self.currentSize:
            mc = self.maxChild(i)  # returns an index

            if self.heapList[i] < self.heapList[mc]:
                self.heapList[mc], self.heapList[i] = self.heapList[i], self.heapList[mc]

            i = mc

    def maxChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] > self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def buildHeap(self, lst):
        i = len(lst) // 2
        self.heapList = [0] + lst[:]
        self.currentSize = len(lst)
        while i > 0:
            self.percDown(i)
            i -= 1

    def maxElem(self):
        return self.heapList[1]

if __name__ == '__main__':
    # Write your code here
    N = int(input())
    lst = list(int(i) for i in input().split())

    # build a max heap out of the list
    heap = MaxHeap()
    heap.buildHeap(lst)

    num_queries = int(input())
    for i in range(num_queries):
        q = list(int(i) for i in input().split())

        if len(q) == 2:
            # this is a type 1 query
            x = q[1]
            # add this element to the list
            heap.insert(x)

        elif len(q) == 1:
            # this is a type 2 query, we just print
            print(heap.maxElem())