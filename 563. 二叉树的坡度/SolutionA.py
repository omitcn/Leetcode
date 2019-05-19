class Solution:
    def __init__(self):
        self.res=0
    def findTilt(self, root):
        if not root:
            return 0
        else:
            self.res+=abs(self.NodeSum(root.left)-self.NodeSum(root.right))
            self.findTilt(root.left)
            self.findTilt(root.right)
        return self.res
    def NodeSum(self,root):
        if not root:
            return 0
        return root.val+self.NodeSum(root.left)+self.NodeSum(root.right)