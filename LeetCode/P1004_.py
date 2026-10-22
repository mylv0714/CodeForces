class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        n = len(nums)
        left = 0
        ans = 0
        cnt = 0

        for right in range(n):
            if nums[right] == 0:
                cnt += 1

            while cnt > k:
                if nums[left] == 0:
                    cnt -= 1
                left += 1

            ans = max(ans,right-left+1)    

        return ans

# arr = [1,1,1,0,0,0,1,1,1,1,0]
# p = Solution().longestOnes(arr,2)
# print(p)