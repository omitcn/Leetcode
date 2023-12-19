# ???•
class Solution:
    def __init__(self):
        self.res = []

    def preorder(self, root):
        if not root:
            return []
        self.res.append(root.val)
        for item in root.children:
            self.preorder(item)
        return self.res
