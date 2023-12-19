class Solution:
    def findWords(self, words):
        l1 = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'}
        l2 = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}
        l3 = {'z', 'x', 'c', 'v', 'b', 'n', 'm'}
        res = []
        for item in words:
            tmp = set(item.lower())
            if tmp.issubset(l1) or tmp.issubset(l2) or tmp.issubset(l3):
                res.append(item)
        return res
