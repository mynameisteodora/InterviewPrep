# Implementation of the Array data structure


class Array:

    def __init__(self, init_array):
        self.length = len(init_array)
        self.internal_array = init_array.copy()

    def assign(self, value, index):
        if index >= self.length or index < 0:
            raise IndexError("Index out of range!")
        else:
            self.internal_array[index] = value

    def insert(self, value, index):
        if index >= self.length or index < 0:
            raise IndexError("Index out of range! Try an index within the range of your list.")

        else:
            # We don't have space anymore and we need to create a bigger array and copy over all the elements
            new_array = [None] * (self.length + 1)
            # Test

            for i in range(index):
                new_array[i] = self.internal_array[i]

            new_array[index] = value

            for i in range(index + 1, self.length+1):
                new_array[i] = self.internal_array[i - 1]

            self.internal_array = new_array.copy()
            print("The new array is: ")
            print(*self.internal_array, sep=',')

    def show(self):
        print("The current array is: ")
        print(*self.internal_array, sep=',')