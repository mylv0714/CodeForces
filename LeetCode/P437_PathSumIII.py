# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        
        def dfs(node:TreeNode, partialSum:int):
            if not node:
                return 0
            
            if partialSum + node.val == targetSum:
                count = 1
            else:
                count = 0

            count += dfs(node.left,partialSum+node.val)
            count += dfs(node.right,partialSum+node.val)

            return count
        
        if not root:
            return 0

        return (dfs(root,0) + 
        self.pathSum(root.left,targetSum) + 
        self.pathSum(root.right,targetSum)
        )

        

# root = [10,5,-3,3,2,None,11,3,-2,None,1]
# targetSum = 8
# nodes = [None if v is None else TreeNode(v) for v in root]
# for i in range(len(nodes)):
#     if nodes[i] is None:
#         continue
#     if 2*i+1 < len(nodes):
#         nodes[i].left = nodes[2*i+1]
#     if 2*i+2 < len(nodes):
#         nodes[i].right = nodes[2*i+2]

# print(Solution().pathSum(nodes[0],targetSum))
# #print(nodes[3].left.val)
