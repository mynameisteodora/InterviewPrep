# Implementation of the Array data structure
import array


class Array:
    # length = 0
    internal_array = []

    # Perhaps I should initialise it with another Array
    def __init__(self, length):
        self.length = length
        self.internal_array = [None] * length

    def assign(self, value, index):
        if index >= self.length or index < 0:
            raise IndexError("Index out of range!")
        else:
            self.internal_array[index] = value

    def insert(self, value, index):

        if index >= self.length or index < 0:
            raise IndexError("Index out of range! Try an index within the range of your list.")

        if self.internal_array[index] == None:
            # This means it is the first time we are adding to that index
            self.internal_array[index] = value

        elif self.internal_array[self.length - 2] == None:
            # This means we still have space in the array and that we can move any elements one position to the right
            for i in range(self.length - 1, index - 1):
                self.internal_array[i] = self.internal_array[i - 1]
                self.internal_array[index] = value
        else:
            # We don't have space anymore and we need to create a bigger array and copy over all the elements
            new_array = [None] * 2 * self.length

            for i in range(index - 1):
                new_array[i] = self.internal_array[i]

            new_array[index] = value

            for i in range(index + 1, self.length):
                new_array[i] = self.internal_array[i - 1]

            self.internal_array = new_array.copy()
            print("The new array is: ")
            print(*self.internal_array, sep=',')
