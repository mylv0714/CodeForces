class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)-1 # nums의 마지막 인덱스 번호
        if n == 0 : 
            return

        left,right = 0,1
        while right <= n:
            if left == right:
                right += 1
                continue

            if nums[right] == 0: # right는 0이아닌자리를 찾도록이동
                right += 1
                continue

            if nums[left] != 0: # left는 0의자리
                left += 1
                continue
            
            nums[left],nums[right] = nums[right],nums[left]
            left += 1
            right += 1
