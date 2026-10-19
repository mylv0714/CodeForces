# Solution1
# n = 4라고 생각해보자. 2 * 4로 만들 수 있는 조합은 아래와 같다.
# 1. n = 3일 때 만든 조합 뒤에 domino (1 * 2)를 붙이는 방법
# 2. n = 2일 때 만든 조합 뒤에 domino (2 * 1)를 두 개 붙이는 방법
# 3. n = 1일 때 만든 조합 뒤에 trominole를 붙일 수 있는 방법 2개
# 4. n = 0일 때 만든 조합 뒤에 trominole과 dominole를 조합해서 붙일 수 있는 방법 2개
# -> trominole로 끝나는 케이스는 전 점화식에 해당이안됨

# dp[n] = dp[n - 1] + dp[n - 2] + 2 * (dp[n - 3] + dp[n - 4] ... + dp[0])
#       = dp[n - 1] + dp[n - 3] + dp[n - 2] + dp[n - 3] + 2 * (dp[n - 4] + ... dp[0])
#       = dp[n - 1] + dp[n - 3] + dp[n - 1]
#       = 2 * dp[n - 1] + dp[n - 3]

# class Solution:
#     def numTilings(self, n: int) -> int:
#         dp = [0]*(n+1)
#         dp[0] = 1
#         dp[1] = 1
#         dp[2] = 2
#         dp[3] = 5
#         for i in range(4,n+1):
#             dp[i] = 2*dp[i-1]+dp[i-3]
        
#         return dp[n]%(1e9+7)


#---------------------------------------------------------------------------------------
# Solution2
# dp[n][0] 2xn 타일의 마지막타일이 깔끔
# dp[n][1] 2=n 타일의 마지막타일이 1개남은경우
class Solution:
    def numTilings(self, n: int) -> int:
        dp = [[0] * 2 for _ in range(n + 1)]
        dp[0][0] = 1
        dp[1][0] = 1

        for i in range(2, n + 1):
            dp[i][0] = (dp[i - 2][0] + dp[i - 1][0] + dp[i - 1][1])
            dp[i][1] = (dp[i - 2][0] * 2 + dp[i - 1][1]) 

        return dp[n][0]%(int(1e9+7))