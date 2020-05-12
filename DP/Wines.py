import numpy as np

class Wines:

    """
    "Imagine you have a collection of N wines placed next to each other on a shelf.
    For simplicity, let's number the wines from left to right as they are standing
    on the shelf with integers from 1 to N, respectively.

    The price of the ith wine is pi. (prices of different wines can be different).

    Because the wines get better every year, supposing today is the year 1, on year y
    the price of the ith wine will be y*pi, i.e. y-times the value that current year.

    You want to sell all the wines you have, but you want to sell exactly one wine per year, starting on this year.
    One more constraint - on each year you are allowed to sell only either the leftmost or the rightmost wine on
    the shelf and you are not allowed to reorder the wines on the shelf
    (i.e. they must stay in the same order as they are in the beginning).

    You want to find out, what is the maximum profit you can get, if you sell the wines in optimal order?"
    """
    def __init__(self, wine_list):
        self.wine_list = wine_list
        self.num_wines = len(wine_list)
        self.cache = [[-1]*self.num_wines for i in range(self.num_wines)]
        self.max_profit = self.profit(0, self.num_wines - 1)

    def profit(self, beg, end):
        print("Calculating profit for beg={}, end={}".format(beg, end))
        print("Current dp = {}".format(self.cache))
        if beg > end:
            return 0

        if self.cache[beg][end] != -1:
            return self.cache[beg][end]
        year = self.num_wines - (end - beg + 1) + 1

        self.cache[beg][end] = max(
            self.profit(beg + 1, end) + year * self.wine_list[beg],
            self.profit(beg, end - 1) + year * self.wine_list[end]
        )

        return self.cache[beg][end]

if __name__ == '__main__':
    wines = [2, 3, 5, 1, 4]
    w = Wines(wines)
    print(w.max_profit)