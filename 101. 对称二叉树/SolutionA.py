# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 递归方法
class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isMirror(root, root)
    def isMirror(self,t1, t2):
        if (not t1) and (not t2):
            return True
        if (not t1) or (not t2):
            return False
        return (t1.val==t2.val) and self.isMirror(t1.right,t2.left) and self.isMirror(t1.left,t2.right)