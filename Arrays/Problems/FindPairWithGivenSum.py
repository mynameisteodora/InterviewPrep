"""
Given an unsorted array of integers, find a pair with a given sum

Example:
    Input = [8, 7, 2, 5, 3, 1]
    sum = 10

    Output: Pair found at indices (0, 2)
"""


class FindPairWithGivenSum:

    def __init__(self, input_list, expected_sum):
        self.input_list = input_list
        self.expected_sum = expected_sum

    def naive_solution(self):
        # This takes O(n^2)

        for i in range(len(self.input_list)):
            for j in range(i, len(self.input_list)):
                if self.input_list[i] + self.input_list[j] == self.expected_sum:
                    return i, j

        return "Pair not found :("

    def better_solution(self):
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

        lst = self.input_list.copy()
        lst.sort()
        high_idx = len(lst) - 1
        low_idx = 0

        while low_idx < high_idx:
            curr_sum = lst[low_idx] + lst[high_idx]

            if curr_sum < self.expected_sum:
                low_idx += 1
            elif curr_sum > self.expected_sum:
                high_idx -= 1
            else:
                return "Pair found!"

        return "Pair not found :("

    def best_solution(self):
        """
        Time complexity: O(n)
        Space complexity: O(n)
        Use a hash map to store value -> index pairs
        At every index, check if target_sum - lst[i] is already in the map
        If it is, it means that we have found the pair and we return the indices
        :return: pair of indices, if found, string otherwise
        """
        hash_map = dict()

        for i in range(len(self.input_list)):
            if self.input_list[i] not in hash_map.keys():
                hash_map[self.input_list[i]] = i

            if self.expected_sum - self.input_list[i] in hash_map.keys():
                return i, hash_map[self.expected_sum - self.input_list[i]]

        return "Pair not found :("


if __name__ == "__main__":

    lst = input("Enter your list of integers, separated by a comma: \n")
    lst = list(map(int, lst.split(",")))

    target_sum = int(input("Enter the target sum: \n"))
    sol = FindPairWithGivenSum(lst, target_sum)

    print("Naive solution: ", sol.naive_solution())

    print("Better solution: ", sol.better_solution())

    print("Best solution: ", sol.best_solution())
