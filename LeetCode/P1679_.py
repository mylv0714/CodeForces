class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        left = 0
        right = len(nums)-1
        ans = 0
        SortL = [*nums]
        SortL.sort()
        while left < right:
            if SortL[left] + SortL[right] == k:
                ans += 1
                left += 1
                right -= 1
            elif SortL[left] + SortL[right] < k:
                left += 1
            else:
                right -= 1
        return ans

#13334