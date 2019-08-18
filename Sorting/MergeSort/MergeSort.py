class MergeSort:

    def merge_sort(self, lst):
        if len(lst) > 1:
            # Find the middle point to divide the array in two halves
            m = len(lst) // 2
            L = lst[:m]
            R = lst[m:]

            # call merge_sort on the first half
            L = self.merge_sort(L)

            # call merge_sort on the second half
            R = self.merge_sort(R)

            # merge the two arrays
            i = j = k = 0

            # while the two halves have the same length,
            # merge the results
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    lst[k] = L[i]
                    i += 1
                else:
                    lst[k] = R[j]
                    j += 1
                k += 1

            # check what elements were left
            while i < len(L):
                lst[k] = L[i]
                k += 1
                i += 1

            while j < len(R):
                lst[k] = R[j]
                k += 1
                j += 1

        return lst

if __name__ == '__main__':
    lst = [4, 5, 1, 7, 23, 63, 0, 3]
    sol = MergeSort()
    print(sol.merge_sort(lst))
