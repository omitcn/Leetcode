class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1 or len(s) == 0:
            return len(s)
        else:
            list1 = list()
            L=len(list1)
            i=0
            while i < len(s):
                s1 = s[i]
                if s1 not in list1:
                    list1.append(s1)
                    i += 1
                    L=L if L>len(list1) else len(list1)
                    continue
                else:
                    j = list1.index(s1) + 1
                    if j == len(list1):
                        list1.clear()
                        list1.append(s1)
                    else:
                        list1 = list1[j:]
                        list1.append(s1)
                        L = L if L > len(list1) else len(list1)
                    i += 1            
            return L
                    

        
        
        
        