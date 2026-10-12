# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# dfs
# class Solution:
#     def maxDepth(self, root: TreeNode | None) -> int:
#         ret = 0
#         def dfs(node: TreeNode | None) -> int:
#             if node == None:
#                 return 0
#             left = dfs(node.left)
#             right = dfs(node.right)
#             return max(left, right) + 1

#         return dfs(root)

# bfs 
from collections import deque

class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        
        q = deque()
        q.append(root)
        ans = 0
        while q:
            ans+= 1
            for _ in range(len(q)):
                popNode = q.popleft()
                if popNode.left:
                    q.append(popNode.left)
                if popNode.right:
                    q.append(popNode.right)

        return ans    
            