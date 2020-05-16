# Given an array of n positive integers and a positive integer s,
# find the minimal length of a contiguous subarray of which the sum IS AT LEAST s.
# If there isn't one, return 0 instead.

# idea: move like an inchworm


def minSubArrayLen(s, nums):

    n = len(nums)
    slow = 0
    fast = 1

    min_len = n
    found = False

    while slow < n - 1 and fast < n:

        # check for the single entry
        if nums[slow] >= s:
            # a single entry matches or exceeds the sum, so we are basically done
            min_len = 1
            found = True
            break

        curr_sum = nums[slow] + nums[fast]
        curr_len = 2
        if curr_sum <= s:
            fast += 1
            while fast < n and curr_sum < s:
                curr_sum += nums[fast]
                fast += 1
                curr_len += 1

        if curr_sum >= s:
            min_len = min(min_len, curr_len)
            found = True

        if fast-slow == 1:
            slow += 1
            fast = slow + 1

        else:
            # only move the slow pointer forward because we might find a sub-array with a suitable sum
            slow += 1

    if found:
        return min_len
    else:
        return 0


if __name__ == "__main__":
    nums = [2, 3, 1, 2, 4, 3]
    s = 7

    result = minSubArrayLen(s, nums)

    print(result)

    nums = [1, 4, 4]
    s = 4

    result = minSubArrayLen(s, nums)

    print(result)

    nums = [1, 2, 3, 4, 5]
    s = 11

    result = minSubArrayLen(s, nums)

    print(result)

    nums = [2, 16, 14, 15]
    s = 20

    result = minSubArrayLen(s, nums)

    print(result)
