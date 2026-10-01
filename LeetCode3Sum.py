# 투 포인터 알고리즘
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        ret = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum3 = nums[i] + nums[left] + nums[right]
                if sum3 == target:
                    return sum3
                else :
                    if abs(sum3 - target) <= abs(ret - target):
                        ret = sum3
                    if sum3 < target:
                        left += 1
                    else:
                        right -= 1
        return ret
        
# Brute Force로 시간초과
"""
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        ret = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    sum3 = nums[i] + nums[j] + nums[k]
                    if sum3 == target:
                        return sum3
                    else :
                        if abs(sum3 - target) < abs(ret - target):
                            ret = sum3
        return ret
"""

list = [-1, 2, 1, -4]
target = 1
res = Solution().threeSumClosest(list,target)

print(res)