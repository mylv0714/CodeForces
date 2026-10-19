class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a','e','i','o','u']
        # 1 <= k <= len(s) <= 10^5
        ans = 0
        for i in range(k):
            if s[i] in vowels:
                ans += 1
        if k == len(s) :
            return ans

        cur = ans
        for i in range(1,len(s)-k+1):
            if s[i-1] in vowels :
                cur -= 1
            if s[i+k-1] in vowels:
                cur += 1
            ans = max(ans,cur)
        return ans