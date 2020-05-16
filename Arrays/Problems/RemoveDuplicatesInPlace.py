# Given an array and a value, remove all instances of that value in-place and return the new length.
# this method uses the fast-runner/slow-runner technique

def removeDuplicates(lst):
    slow_runner = 0
    fast_runner = 1

    n = len(lst)

    new_list = [None] * n

    while fast_runner < n:

        if lst[fast_runner] != lst[slow_runner]:
            slow_runner += 1

        lst[slow_runner] = lst[fast_runner]
        new_list[slow_runner] = lst[fast_runner]
        fast_runner += 1


    return lst[:slow_runner+1], slow_runner+1

if __name__ == "__main__":
    lst = [0,1,1,1,3,4,5]

    ans, size = removeDuplicates(lst)

    print(ans)
    print(size)