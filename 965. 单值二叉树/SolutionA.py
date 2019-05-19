class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        list1 = list()
        list1.append(root)
        for x in list1:
            if x.right != 'null' and x.right !=None :
                list1.append(x.right)
                temp = x.right
                if temp.val != x.val:
                    return False
            if x.left != None and x.left!='null':
                list1.append(x.left)
                temp = x.left
                if temp.val != x.val:
                    return False
        return True
