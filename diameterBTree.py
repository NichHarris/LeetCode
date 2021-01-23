# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 1
        def dfs(node):
            if not node: return 0
            
            l =  dfs(node.left)
            r = dfs(node.right)
            
            self.ans = max(self.ans, l+r+1)
            return max(l, r) + 1
        
        dfs(root)
        return self.ans - 1