import heapq
class Solution:    
    def findKthLargest(self, nums: list[int], k: int) -> int:
        hq = []
        for num in nums:
            heapq.heappush(hq,num)

        while len(hq) > k:
            heapq.heappop(hq)

        return hq[0]

        

# nums = [3,2,1,5,6,4]
# print(Solution().findKthLargest(nums,2))