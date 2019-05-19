# 递归法
class Solution:
    def __init__(self):
        self.res = []

    def postorder(self, root):
        if not root:
            return []
        for item in root.children:
            self.postorder(item)
            self.res.append(item.val)
        return self.res
