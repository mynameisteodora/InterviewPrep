# Determine if a string has all unique characters

class HasAllUniqueCharacters:

    def __init__(self, str):
        self.str = str

    def all_chars_unique_1(self):
        if len(self.str) > 128:
            return False

        char_set = [False]*128

        for i in range(len(self.str)):
            # TODO - how do you represent ascii codes in python?
            if char_set[self.str[i]]:
                return False
            else:
                char_set[self.str[i]] = True

        return True

    def all_chars_unique_2(self):
        # TODO - bit operations in python
        return True

if __name__ == '__main__':
    test_str = HasAllUniqueCharacters("teodora")
    print(test_str.all_chars_unique_1())


