class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        ans = 0
        sum = 0
        for i in range(len(gain)):
            sum += gain[i]
            ans = max(ans,sum)
        return ans