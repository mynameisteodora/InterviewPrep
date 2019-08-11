# This is where I test my implementation of Array
import Arrays.Implementation.Array as myArr


if __name__ == "__main__":

    # Initialise array
    myArray = myArr.Array([1,2,3,4])
    myArray.show()

    # Assign a value to an index
    myArray.assign(92, 0)
    myArray.show()

    # Observe what happens to the array when we insert a new element
    myArray.insert(452, 2)


