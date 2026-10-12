from collections import deque

class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        m,n = len(maze), len(maze[0])
        visited = [[0]*n for _ in range(m)]

        ent_row,ent_col = entrance
        visited[ent_row][ent_col] = 1
        q = deque() 
        q.append((ent_row,ent_col,0)) # row,col,dist
    
        dy = [0,0,1,-1]
        dx = [1,-1,0,0]
        while q:
            i,j,dist = q.popleft()

            if (i,j) != (ent_row,ent_col):
                if i==0 or i==m-1 or j==0 or j==n-1:
                    return dist

            for k in range(4):
                ni = i + dy[k]
                nj = j + dx[k]
                if 0<=ni<=m-1 and 0<=nj<=n-1:
                    if not visited[ni][nj] and maze[ni][nj] == '.':
                        visited[ni][nj] = 1
                        q.append((ni,nj,dist+1))

        return -1