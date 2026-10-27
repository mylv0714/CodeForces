# bit brute-force
# class Solution:
#     def countBits(self, n: int) -> list[int]:
#         ansArr = []
#         for i in range(n+1):
#             ans = 0
#             for c in range(20):
#                 ans += (i >> c) & 1
#             ansArr.append(ans)
#         return ansArr

# dp solution
class Solution:
    def countBits(self, n: int) -> list[int]:
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)

        return dp