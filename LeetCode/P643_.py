class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        n = len(nums) 
        cur = sum(nums[:k])
        ans = cur
        
        for i in range(k,n):
            cur += nums[i] - nums[i-k]
            ans = max(ans,cur)
        return ans/k

# t1 = [1,12,-5,-6,50,3]
# k= 4
# t1 = [0,4,0,3,2]
# k = 1
# f = Solution().findMaxAverage(t1,k)
# print(f)
