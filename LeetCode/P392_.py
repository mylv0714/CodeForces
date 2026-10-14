class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sLen,tLen = len(s),len(t)
        if sLen > tLen: 
            return False
        
        sIndex = 0
        for i in t:
            if sIndex < sLen and s[sIndex] == i:
                sIndex += 1
        
        return sIndex == sLen

# print(Solution().isSubsequence("abc","ahbgdc"))
# print(Solution().isSubsequence("axc","ahbgdc"))
            
            