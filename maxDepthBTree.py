# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        result = 0
        
        if root == None:
            return result
        else:
            depthLeft = self.maxDepth(root.left)    
            depthRight =  self.maxDepth(root.right)
            # PLus one from root node
            result = max(depthLeft, depthRight) + 1
        
        return result