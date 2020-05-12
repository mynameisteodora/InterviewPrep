class Fibonacci:

    def fib_recursive(self, n):
        # returns the n-th fibonacci number
        if n == 0 or n == 1:
            return 1
        else:
            return self.fib_recursive(n-1) + self.fib_recursive(n-2)

    def fib_dp(self, n):
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        print("DP array: {}".format(dp))
        return dp[n]

if __name__ == '__main__':
    f = Fibonacci()
    print(f.fib_recursive(30))
    print(f.fib_dp(30))