class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word3 = []
        for i in range(len(word1)):
            word3.append(word1[i])
            if i < len(word2):
                word3.append(word2[i])

        if len(word2) > len(word1):
            for j in range(len(word1), len(word2)):
                word3.append(word2[j])

        return "".join(word3)


# word1 = "abcd"
# word2 = "pq"
# word3 = Solution().mergeAlternately(word1, word2)
# print(word3)