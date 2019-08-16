import unittest

from Arrays.Problems.FindPairWithGivenSum import FindPairWithGivenSum


class MyTestCase(unittest.TestCase):

    def test_naive_solution(self):
        input_list = [1, 2, 3, 4, 5]
        expected_sum = 5
        sol = FindPairWithGivenSum(input_list, expected_sum)
        self.assertEqual((0, 3), sol.naive_solution())

    def test_better_solution(self):
        input_list = [3, 5, 1, 1, 2, 52, 34]
        expected_sum = 7
        sol = FindPairWithGivenSum(input_list, expected_sum)
        self.assertEqual("Pair found!", sol.better_solution())

    def test_best_solution(self):
        input_list = [2, 52, 4, 2, 1, 5, 2, 1, 4, 1, 3, 5, 67, 1, 7, 3, 7, 9, 3]
        expected_sum = 68
        sol = FindPairWithGivenSum(input_list, expected_sum)
        self.assertEqual((4, 12), tuple(sorted(sol.best_solution())))


if __name__ == '__main__':
    unittest.main()
