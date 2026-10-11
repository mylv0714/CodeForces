class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split()
        l.reverse()
        return " ".join(l)


# S = "the sky is blue"
# rS = Solution().reverseWords(S)
# print(rS)