# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node : TreeNode, maxval:int) -> int:
            cnt = 0
            if node == None:
                return 0
            
            if node.val >= maxval:
                cnt += 1
                maxval = node.val

            return cnt + dfs(node.left,maxval) + dfs(node.right,maxval)
        
        return dfs(root,root.val)