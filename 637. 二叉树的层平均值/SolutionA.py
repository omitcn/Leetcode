class Solution:
    def averageOfLevels(self, root):
        if not root:
            return []
        superstratum = [root]
        subsratum = []
        res = []
        tmp=0
        while superstratum:
            for item in superstratum:
                tmp += item.val
                if item.left:
                    subsratum.append(item.left)
                if item.right:
                    subsratum.append(item.right)
            res.append(tmp / len(superstratum))
            tmp, superstratum, subsratum = 0, subsratum, []
        return res