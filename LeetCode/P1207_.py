class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        dic = {}
        for a in arr:
            dic[a] = dic.get(a,0) + 1
        
        return len(dic.values()) == len(set(dic.values()))


# dic = {}
# arr = ['1']
# dic[arr[0]] = 1
# dic[arr[0]] += 1

# print(len(dic.values()))