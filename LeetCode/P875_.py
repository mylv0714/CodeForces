from math import ceil


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        piles.sort()
        left = 1
        right = piles[len(piles)-1]

        ans = right
        while left <= right:
            mid = (left+right)//2
            sum = 0
            for p in piles:
                sum += ceil(p/mid)
            
            if sum <= h:
                ans = min(ans,mid)
                right = mid-1
            else:
                left = mid+1
        
        return ans

list = [3,6,7,11]
print(Solution().minEatingSpeed(list,8))