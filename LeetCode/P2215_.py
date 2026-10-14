class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        answer = [ [] for _ in range(2) ]
        answer[0] = list(set1-set2)
        answer[1] = list(set2-set1)
        return answer
        


# nums1 = [1,2,3]
# nums2 = [2,4,6]
# set1 = set(nums1)
# set2 = set(nums2)

# list1 = [set1.difference(set2)]
# set2.issubset
