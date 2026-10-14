class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        newlist = [*flowerbed]
        length = len(newlist)

        if n == 0 : return True

        # length <= 2
        if length == 1:
            if newlist[0] == 0:
                if n<=1:
                    return True
                else:
                    return False
            else:
                return False
        elif length == 2:
            if newlist[0]== 1 or newlist[1] == 1:
                return False
            else:
                if n <= 1:
                    return True
                else:
                    return False

        # length >= 3
        for i in range(1,length-1):
            if flowerbed[i] == 1 :
                newlist[i-1] = 1
                newlist[i+1] = 1
        if flowerbed[0] == 1 : newlist[1] = 1
        if flowerbed[length-1] == 1 : newlist[length-2] = 1
        #print(newlist)
        canSeat = 0
        for i in range(length-1):
            if newlist[i] == 0:
                canSeat += 1
                newlist[i+1] = 1
        
        if newlist[length-2] == 1 and newlist[length-1] == 0:
            canSeat += 1
        
        return canSeat >= n

# list = [1,0,0,0,1,0,0]
# n = 2
# print(Solution().canPlaceFlowers(list,n))


#Better clean Code : list index 오류를 피하기위해 empty_left_plot, empty_right_plot
#                    에서 or연산자 앞에 index 검사를 먼저하는게 포인트

# class Solution:
#     def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
#         count = 0
#         for i in range(len(flowerbed)):
#             # Check if the current plot is empty.
#             if flowerbed[i] == 0:
#                 # Check if the left and right plots are empty.
#                 empty_left_plot = (i == 0) or (flowerbed[i - 1] == 0)
#                 empty_right_lot = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                
#                 # If both plots are empty, we can plant a flower here.
#                 if empty_left_plot and empty_right_lot:
#                     flowerbed[i] = 1
#                     count += 1
                    
#         return count >= n