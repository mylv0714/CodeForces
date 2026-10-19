class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        dp = [0]*n
        dp[0],dp[1] = cost[0],cost[1]
        for i in range(2,n):
            dp[i] = min(dp[i-1]+cost[i], dp[i-2]+cost[i])
            #print("i의값 :", i, "\n", "dp의값 :", dp[i])
        return min(dp[n-1],dp[n-2])