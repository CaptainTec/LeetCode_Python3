# class Solution:
#     def f(self, n, i, k):
#         if (self.tmp[n][i][k] != -1):
#             return self.tmp[n][i][k]
#         if n == 0 or k == 0 or i == 0:
#             self.tmp[n][i][k] = 0
#             return 0
#         if n == 1 and k == 1:
#             self.tmp[n][i][k] = 1
#             return 1
#         r=0
#         for j in range(1, i):
#             r += self.f(n-1, j, k-1)
#             r %= 1000000007
#         r += self.f(n-1, i, k)*i
#         r %= 1000000007
#         self.tmp[n][i][k] = r
#         return r
#     # def numOfArrays(self, n: int, m: int, k: int) -> int:
#     def numOfArrays(self, n, m, k):
#         self.tmp = [[[-1 for t in range(k+1)] for j in range(m+1)] for i in range(n+1)]
#         r = 0
#         for i in range(1, m+1):
#             r += self.f(n, i, k)
#             r %= 1000000007
#         return r


class Solution:
    # def numOfArrays(self, n: int, m: int, k: int) -> int:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        mod = 1000000007
        dp = [[[0 for i in range(k+1)] for j in range(m+1)] for a in range(n+1)]
        for i in range(1, m+1):
            for j in range(1, k + 1):
                if j > 1:
                    dp[1][i][j] = 0
                else:
                    dp[1][i][j] = 1
        for i in range(1, n+1):
            for j in range(1, k + 1):
                if j == 1:
                    dp[i][1][j] = 1
                else:
                    dp[i][1][j] = 0
        
        for i in range(2, n + 1):
            for j in range(2, m + 1):
                for a in range(1, k+1):
                    for b in range(1, j):
                        dp[i][j][a] += dp[i-1][b][a-1]
                        dp[i][j][a] %= mod
                    dp[i][j][a] += j * dp[i-1][j][a]
                    dp[i][j][a] %= mod
        res = 0
        for i in range(1, m+1):
            res += dp[n][i][k]
            res %= mod
        return res
            

Solution().numOfArrays(1, 2, 3)
