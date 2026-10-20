class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        n = len(grid)
        rowdic = {}
        coldic = {}
        for arr in grid:
            arr = tuple(arr)
            rowdic[arr] = rowdic.get(arr,0) + 1
        for j in range(n):
            col = []
            for i in range(n):
                col.append(grid[i][j])
            col = tuple(col)
            coldic[col] = coldic.get(col,0) + 1

        ans = 0
        for key,val in rowdic.items():
            ans += val * coldic.get(key,0)

        return ans