class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiou')
        v_idx = []
        for i in range(len(s)):
            if s[i].lower() in vowels:
                v_idx.append(i)

        s = list(s)
        
        n = len(v_idx)
        for i in range(n//2):
            left = v_idx[i]
            right = v_idx[n-1-i]
            s[left],s[right] = s[right],s[left]
            
        return ''.join(s)
