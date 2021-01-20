# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
                  
        def bst(root, k, hashMap):
                 
            if root == None:
                return False
            
            complement = k - root.val
            if complement in hashMap:
                return True
            
            hashMap[root.val] = k
        
            return bst(root.left, k, hashMap) or bst(root.right, k, hashMap)
        
        hashMap = {}
        return bst(root, k, hashMap)