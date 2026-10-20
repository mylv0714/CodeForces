# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        cur = root
        while cur and cur.val != key:
            prev = cur
            if cur.val < key:
                cur = cur.left
            else:
                cur = cur.right

        if cur.val == key:
            if prev.val > key: #delete node가 왼쪽자식인경우
                if cur.left:
                    
                elif cur.right:
                prev.left = cur.left.right
            

        return root 