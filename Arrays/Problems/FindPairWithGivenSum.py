"""
Given an unsorted array of integers, find a pair with a given sum

Example:
    Input = [8, 7, 2, 5, 3, 1]
    sum = 10

    Output: Pair found at indices (0, 2)
"""

if __name__ == "__main__":

    lst = input("Enter your list of integers, separated by a comma: \n")
    lst = list(map(int, lst.split(",")))

    target_sum = int(input("Enter the target sum: \n"))
    print(target_sum)


    def naive_solution():
        # This takes O(n^2)

        for i in range(len(lst)):
            for j in range(i, len(lst)):
                if lst[i] + lst[j] == target_sum:
                    return i, j

        return "Pair not found :("


    print("Pair found at indices: ", naive_solution())

    def better_solution():
        """
        Time complexity: O(nlogn) 
        We sort the array and we keep two indices, 
        one at the beginning of the array and one at the end
        We start by adding the first and last element
        If the sum in less than target_sum, we increase low_idx
        Otherwise we decrease high_idx
        When we find a matching pair we return success
        If we've reached the middle and no sum was found we return failure
        This method DOES NOT return the original indices of the found pair
        :return: 
        """""

        lst.sort()
        high_idx = len(lst) - 1
        low_idx = 0

        while low_idx < high_idx:
            curr_sum = lst[low_idx] + lst[high_idx]

            if curr_sum < target_sum:
                low_idx += 1
            elif curr_sum > target_sum:
                high_idx -= 1
            else:
                return "Pair found!"

        return "Pair not found :("

    print(better_solution())

    def best_solution():
        """
        Time complexity: O(n)
        Space complexity: O(n)
        Use a hash map to store value -> index pairs
        At every index, check if target_sum - lst[i] is already in the map
        If it is, it means that we have found the pair and we return the indices
        :return: pair of indices, if found, string otherwise
        """
        hash_map = dict()

        for i in range(len(lst)):
            if lst[i] not in hash_map.keys():
                hash_map[lst[i]] = i

            if target_sum-lst[i] in hash_map.keys():
                return i, hash_map[target_sum-lst[i]]

        return "Pair not found :("

    print(best_solution())



