# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        qlist = [root]
        res = list()
        while True:
            temp = list()
            tmp=list()                
            for x in qlist:
                temp.append(x.val)
                if x.left:
                    tmp.append(x.left)
                if x.right:
                    tmp.append(x.right)
            res.append(temp)
            if tmp:
                qlist = tmp
                continue
            break
        return res
# 第107题 二叉树的层次遍历II,其他不变, 返回 return res[::-1]即可
