from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode | None) -> int:
        q = deque()
        q.append(root)
        ans_level = 1
        ans_val = root.val
        cur_level = 1
        while len(q) > 0:
            cur_val = 0
            for _ in range(len(q)):
                curNode = q.popleft()
                cur_val += curNode.val
                if curNode.left: q.append(curNode.left)
                if curNode.right: q.append(curNode.right)
            if cur_val > ans_val :
                ans_val = cur_val
                ans_level = cur_level
            cur_level += 1

        return ans_level