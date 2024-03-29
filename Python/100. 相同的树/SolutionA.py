#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        elif p or q:
            try:
                return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)) if p.val==q.val else False
            except:
                return False