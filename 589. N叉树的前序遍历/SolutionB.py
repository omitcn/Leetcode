# 迭代解法
class Solution:
    def preorder(self, root):
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.children:
                stack+=node.children[::-1]
        return res