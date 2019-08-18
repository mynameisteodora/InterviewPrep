class SubArraysWithGivenSum:

    def __init__(self, lst, target_sum):
        self.lst = lst
        self.target_sum = target_sum

    def solution(self):
        my_map = dict()
        curr_sum = 0
        answers = list()

        for idx, val in enumerate(self.lst):
            curr_sum += val

            if curr_sum - self.target_sum in my_map.keys():
                # we have found a subarray with the target_sum
                initial_idx = my_map[curr_sum - self.target_sum]
                answers.append((initial_idx + 1, idx))

            my_map[curr_sum] = idx

        if(len(answers)):
            return answers
        else:
            return "No subarray found"

if __name__ == '__main__':
    lst = [4,2,-3,-1,0,4]
    target_sum = -231

    sol = SubArraysWithGivenSum(lst, target_sum)
    print(sol.solution())
