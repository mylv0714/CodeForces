# Bottom-up approach
# class Solution:
#     def maxProfit(self, prices: list[int], fee: int) -> int:
#         n = len(prices)
#         dp = [ [0] * 2 for _ in range(n+1) ]
#         dp[1][0] = 0
#         dp[1][1] = -prices[0]
#         for i in range(2,n+1):
#             dp[i][0] = max(dp[i-1][1] + prices[i-1]-fee, dp[i-1][0])
#             dp[i][1] = max(dp[i-1][1],dp[i-1][0]-prices[i-1])
#         return dp[n][0]

# Top-down approach

from functools import cache
class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        n = len(prices)
        
        @cache
        def dp(i, hold=0) -> int:
            
            if i==1:
                if hold == 0:
                    return 0
                else:
                    return -prices[0]
            
            if hold == 0:
                return max(dp(i-1,1)+prices[i-1]-fee, dp(i-1,0))
            else:
                return max(dp(i-1,1),dp(i-1,0)-prices[i-1])
            
        return dp(n,0)
