class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x:x[1])
        ans = 1
        end = points[0][1]
        for i in range(len(points)):
            if points[i][0] <= end <= points[i][1]:
                pass
            else:
                ans += 1
                end = points[i][1]
        return ans

#[[1,6],[2,8],[7,12],[10,16]]