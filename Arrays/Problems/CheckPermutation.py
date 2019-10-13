# Check if string 1 is the permutation of string 2

class CheckPermutation:

    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2

    def is_permutation(self):
        if len(self.s1) != len(self.s2):
            return False

        hash_map = dict()

        for i in range(len(self.s1)):
            val = self.s1[i]
            if val in hash_map.keys():
                hash_map[val] += 1
            else:
                hash_map[val] = 1

        for i in range(len(self.s2)):
            val = self.s2[i]
            if val not in hash_map.keys():
                return False
            elif hash_map[val] == 0:
                return False
            else:
                hash_map[val] -= 1

        return True

if __name__ == '__main__':
    s1 = input("Enter the first string:")
    s2 = input("Enter the second string:")
    print("Are they permutations?")
    answer = CheckPermutation(s1, s2)
    print(answer.is_permutation())