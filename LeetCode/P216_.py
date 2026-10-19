class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        ans = []
        path = []

        def dfs(start,remain):
            if len(path) == k:
                if remain == 0:
                    ans.append(path[:])
                return
            
            for num  in range(start,10):
                path.append(num)
                dfs(num+1,remain-num)
                path.pop()
        
        dfs(1,n)
        return ans