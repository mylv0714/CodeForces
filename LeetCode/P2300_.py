class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        potions.sort()
        ans = []
        for s in spells:
            left = 0
            right = len(potions)-1
            while left <= right:
                mid = (left+right)//2
                if s * potions[mid] >= success:
                    right = mid-1
                else:
                    left = mid+1
            ans.append(len(potions)-right-1)
        return ans
