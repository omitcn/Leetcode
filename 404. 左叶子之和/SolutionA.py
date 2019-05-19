class Solution:
    sum=0
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        TreeQ=list()
        if not root:
            return 0
        l=root.left
        r=root.right
        if l and (not l.left) and (not l.right):
            return l.val+self.sumOfLeftLeaves(r)
        else:
            return self.sumOfLeftLeaves(root.left)+self.sumOfLeftLeaves(root.right)