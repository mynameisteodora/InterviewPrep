def longestCommonPrefix(strs):

    if len(strs) == 0:
        return ""

    longest_prefix = strs[0]

    for i in range(len(strs)):
        current_word = strs[i]

        for j in range(min(len(longest_prefix), len(current_word))):
            if longest_prefix[j] != current_word[j]:
                break
            j+= 1

        longest_prefix = current_word[:j]

        if j == 0:
            longest_prefix = ""

    return longest_prefix



if __name__ == "__main__":
    strs = ["flower","flow","flight"]

    result = longestCommonPrefix(strs)

    print(result)