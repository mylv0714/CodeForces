class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left = 0
        right = len(nums)-1

        if right == 0:
            return 0
    
        while left < right:
            mid = (left+right)//2
            if nums[mid] < nums[mid+1]:
                left = mid+1
            else:
                right = mid

        return left
