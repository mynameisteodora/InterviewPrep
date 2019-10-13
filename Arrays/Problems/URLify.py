# Write a method to replace all the spaces in a string with '%20'

class URLify:

    def __init__(self, url):
        self.url = url

    def urlify(self):
        num_spaces = 0

        for i in range(len(self.url)):
            if self.url[i] == ' ':
                num_spaces += 1

        new_len = len(self.url) + num_spaces * 3
        final_str = ""

        for i in range(len(self.url), 0, -1):
            curr_char = self.url[i-1]

            if curr_char == ' ':
                final_str += "02%"
            else:
                final_str += curr_char

        # TODO - how do you reverse a string??
        return reversed(final_str)

if __name__ == '__main__':
    s = input("Enter a string to urlify")
    answer = URLify(s)
    print(answer.urlify())

