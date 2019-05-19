class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        res = []
        queue = [root]
        tmp = []
        temp = []
        while queue:
            for item in queue:
                temp.append(item.val)
                tmp += item.children
            res.append(temp)
            queue, tmp, temp = tmp, [], []
        return res