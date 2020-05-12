import numpy as np

class LongestSubsequence:

    def print_dp(self, dp):
        m, n = np.shape(dp)
        for i in range(m):
            print(dp[i])

        print('-'*80)

    def find_longest_subsequence(self, x, y):
        # initialise a dp matrix of size
        # [len(x) + 1] * [len(y) + 1]
        n = len(x)
        m = len(y)
        dp = np.zeros((n+1, m+1))
        self.print_dp(dp)

        # start populating the table
        for i in range(n+1):
            for j in range(m+1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif x[i-1] == y[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    self.print_dp(dp)
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    self.print_dp(dp)

        def reconstruct(i, j):
            if i == 0 or j == 0:
                return []
            elif x[i - 1] == y[j - 1]:
                return reconstruct(i - 1, j - 1) + [x[i - 1]]
            elif dp[i][j] == dp[i - 1][j]:
                return reconstruct(i - 1, j)
            else:
                return reconstruct(i, j - 1)

        print(*reconstruct(n, m))




if __name__ == '__main__':
    l = LongestSubsequence()
    l.find_longest_subsequence('abcddef', 'acdeff')

