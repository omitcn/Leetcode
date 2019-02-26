class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        TreeQ=list()
        if not root:
            return
        l=self.sumOfLeftLeaves(root.left)