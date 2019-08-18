class BubbleSort:

    def __init__(self, lst):
        self.lst = lst

    def sort(self, ascending=True):
        n = len(self.lst)

        if (ascending):
            for i in range(n):
                swapped = False

                for j in range(n - i - 1):

                    if self.lst[j] > self.lst[j + 1]:
                        self.lst[j], self.lst[j + 1] = self.lst[j + 1], self.lst[j]
                        swapped = True

                if not swapped:
                    break
        else:
            for i in range(n):
                swapped = False

                for j in range(n - i - 1):

                    if self.lst[j] < self.lst[j + 1]:
                        self.lst[j], self.lst[j + 1] = self.lst[j + 1], self.lst[j]
                        swapped = True

                if not swapped:
                    break

        return self.lst

    def recursive_sort(self, my_lst, list_length, ascending = True):
        if list_length == 1:
            return my_lst

        else:
            if(ascending):
                for i in range(list_length-1):
                    if my_lst[i] > my_lst[i+1]:
                        my_lst[i], my_lst[i+1] = my_lst[i+1], my_lst[i]
                return self.recursive_sort(my_lst, list_length - 1, True)
            else:
                for i in range(list_length-1):
                    if my_lst[i] < my_lst[i+1]:
                        my_lst[i], my_lst[i+1] = my_lst[i+1], my_lst[i]

                return self.recursive_sort(my_lst, list_length - 1, False)



if __name__ == '__main__':
    lst = [3, 2, 5, 2, 7, 43, 1, 53, 123]
    sol = BubbleSort(lst)
    print(sol.sort(False))

    print(sol.recursive_sort(lst, len(lst), False))