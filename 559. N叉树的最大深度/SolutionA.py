class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        elif not root.children:
            return 1
        else:
            res = []
            for child in root.children:
                res.append(self.maxDepth(child)+1)
            return max(res)
