class QuickSort:

    def quick_sort(self, lst):
        n = len(lst)

        if n < 2:
            # This list is already sorted
            return lst

        pivot = lst[-1]
        L = []
        E = []
        G = []

        while len(lst) > 0:
            curr_elem = lst.pop(0)
            if curr_elem < pivot:
                L.append(curr_elem)
            elif curr_elem == pivot:
                E.append(curr_elem)
            else:
                G.append(curr_elem)

        L = self.quick_sort(L)
        G = self.quick_sort(G)

        while len(L) > 0:
            lst.append(L.pop(0))

        while len(E) > 0:
            lst.append(E.pop(0))

        while len(G) > 0:
            lst.append(G.pop(0))

        return lst

if __name__ == '__main__':
    qs = QuickSort()
    lst = [5,2,5,1,6,36,8,325,275,942,251,24]
    print(qs.quick_sort(lst))