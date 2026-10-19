class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key = lambda x : x[1])
        ans = 0
        prev_end = int(-5*1e4)
        for i in intervals:
            start,end = i[0],i[1]
            if start >= prev_end:
                prev_end = end
            else:
                ans += 1
        return ans

# arr = [[1,2],[3,6],[4,2],[5,4]]
# arr.sort(key=lambda x:x[1])
# print(arr)