class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        str_x = str(x)
        list1 = []
        list2 = []
        for i in range(len(str_x)):
            list1.append(str_x[i])
        for i in range(len(str_x)-1,-1,-1):
            list2.append(str_x[i])
        # print(list1)
        # print(list2)
        return list1 == list2     
