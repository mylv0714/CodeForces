class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        left = 0
        right = 0
        ans = 0
        zerocnt = 0

        while right < len(nums):
            if nums[right] == 0:
                zerocnt += 1
            while zerocnt > 1:
                if nums[left] == 0:
                    zerocnt -= 1
                left += 1

            ans = max(ans,right-left+1)
            right +=1

        return ans-1