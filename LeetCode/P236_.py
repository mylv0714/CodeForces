# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def findNode(root: 'TreeNode', target: 'TreeNode', pList:list):
            if root is None:
                return
            
            pList.append(root)
            if root == target:
                return pList
            
            result = findNode(root.left,target,pList)
            if result is not None:
                return result

            result = findNode(root.right,target,pList)
            if result is not None:
                return result
            
            pList.pop() # memory management
            return None

        pArr, qArr = [], []
        p_Arr, q_Arr = findNode(root,p,pArr), findNode(root,q,qArr)
        p_set = set()
        for p in p_Arr:
            p_set.add(p)
        
        for i in range(len(q_Arr)-1,-1,-1):
            if q_Arr[i] in p_set:
                return q_Arr[i]

# Clean Solution DFS
# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode',
#                              p: 'TreeNode',
#                              q: 'TreeNode') -> 'TreeNode':

#         if root is None or root == p or root == q:
#             return root

#         left = self.lowestCommonAncestor(root.left, p, q)
#         right = self.lowestCommonAncestor(root.right, p, q)

#         if left and right:
#             return root

#         return left if left else right