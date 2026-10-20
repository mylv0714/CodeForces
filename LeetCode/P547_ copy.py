class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        visited = [0]*n

        def dfs(start):
            visited[start] = True
            for i in range(n):
                if isConnected[start][i] and not visited[i]:
                    dfs(i)

        ans = 0
        for i in range(n):
            if not visited[i]:
                ans += 1
                dfs(i)

        return ans