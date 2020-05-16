# Find the maximum length of the subarray which contains only 1s

def findMaxConsecutiveOnes(nums):
    n = len(nums)
    beg = 0
    end = 1

    max_len = 0

    while beg <= n-1:
        if nums[beg] == 1:
            curr_len = 1
            while end < n:
                if nums[end] == 1:
                    curr_len += 1
                    end += 1
                else:
                    break
            max_len = max(max_len, curr_len)
        beg = end
        end = beg + 1

    return max_len

if __name__ == "__main__":
    nums = [1,1,0,0,1,1,1,1]

    result = findMaxConsecutiveOnes(nums)

    print(result)