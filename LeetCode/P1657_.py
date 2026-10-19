class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        set1 = {}
        set2 = {}

        for w in word1 :
            set1[w] = set1.get(w,0) + 1

        for w in word2 :
            set2[w] = set2.get(w,0) + 1
        
        if set1.keys() != set2.keys():
            return False

        if sorted(set1.values()) != sorted(set2.values()):
            return False
        
        return True