# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        def dfs(node: TreeNode, l: list[int]):
            if node.left == None and node.right == None:
                l.append(node.val)
            else:
                if node.left:
                    dfs(node.left, l)
                if node.right:
                    dfs(node.right, l)
        l1 = []
        l2 = []
        dfs(root1, l1)
        dfs(root2, l2)
        return l1 == l2