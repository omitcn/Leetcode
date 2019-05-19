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
                    j = 0
                    while list1[j]!=s1:
                        del list1[j]
                    del list1[j]
                    list1.append(s1)
                    L = L if L > len(list1) else len(list1)
                    i += 1
            return L
                    