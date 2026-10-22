# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode | None) -> int:
        ans = 0
        def dfs(Node: TreeNode | None, direction, depth):
            nonlocal ans

            if Node is None :
                return
            
            ans = max(ans,depth)
            
            if direction == "left":
                dfs(Node.right,"right",depth+1)
                dfs(Node.left,"left",1)
            elif direction == "right":
                dfs(Node.left,"left",depth+1)
                dfs(Node.right,"right",1)

        dfs(root,"left",0)
        dfs(root,"right",0)
        return ans