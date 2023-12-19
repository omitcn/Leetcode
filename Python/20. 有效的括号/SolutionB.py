class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 == 1:
            return False
        list1 = list(s)
        list2 = list()
        list3 = {')': '(', ']': '[', '}': '{'}
        for i in range(len(s)):
            if list1[i] == "{" or list1[i] == "(" or list1[i] == "[":
                list2.append(list1[i])
                continue
            else:
                if not len(list2):
                    return False
                else:
                    t = list2.pop()
                    list2.append(t)
                    if len(list2) and t == list3[list1[i]]:
                        list2.pop()          
        if len(list2):
            return False
        return True