class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        visited = [0]*len(rooms)
        def dfs(startNum:int):
            for room in rooms[startNum]:
                if not visited[room]:
                    visited[room] = True
                    dfs(room)
        
        visited[0] = True
        dfs(0)

        for i in range(len(rooms)):
            if not visited[i]:
                return False 
        return True

# rooms = [[1],[2],[3],[]]
# print(Solution().canVisitAllRooms(rooms))