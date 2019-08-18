class SelectionSort:

    def __init__(self, lst):
        self.lst = lst

    def sort(self):
        n = len(self.lst)

        for i in range(n):
            min = self.lst[i]
            min_idx = i

            for j in range(i, n):
                if self.lst[j] < min:
                    min = self.lst[j]
                    min_idx = j

            self.lst[i], self.lst[min_idx] = self.lst[min_idx], self.lst[i]

        return self.lst


if __name__ == '__main__':
    lst = [1, 4, 1, 5, 26, 23, 23, 44, 2341, 24]
    sol = SelectionSort(lst)
    print(sol.sort())
