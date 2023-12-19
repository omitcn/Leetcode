class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 == 1:
            return False
        list1 = list(s)
        len1 = len(s)
        list2 = list()
        cnt = 0
        list3 = {')': '(', ']': '[', '}': '{'}
        list4=['[','{','(']
        for i in range(len1):
            if list1[i] in list4:
                list2.append(list1[i])
                cnt += 1
                continue
            else:
                cnt += 1
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

        
                
            
        

            
            
        