class Solution:
    def make_dp(self, nums: list[int]) -> int:
        dp = [0]*len(nums)
        dp[0] = nums[0]
        if len(nums) <= 1:
            return nums[0]
        else:
            dp[1] = max(nums[0], nums[1])
            
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[-1]

    def rob(self, nums: list[int]) -> int:
        return self.make_dp(nums)


# t1 = [1,2,3,1]
# ans1 = Solution().rob(t1)
# print(ans1)

# t2 = [2,7,9,3,1]
# ans2 = Solution().rob(t2)
# print(ans2)