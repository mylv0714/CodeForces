# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# ans = 6
# def guess(num: int) -> int:
#     if num > ans:
#         return -1
#     elif num < ans:
#         return 1
#     else:
#         return 0
    

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        while left < right:
            mid = (left+right)//2
            ret = guess(mid)
            if ret == -1:
                right = mid
            elif ret == 1:
                left = mid+1
            else:
                return mid
        return left
        

# print(Solution().guessNumber(10))