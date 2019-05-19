class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        tmp=s[::-1]
        i,slen=0,len(s)
        while i<slen:
            if tmp[i]==' ':
                i+=1
                continue
            break
        if i<slen:
            j=i
            while j<slen and tmp[j]!=' ':
                j+=1
            return j-i
        else:
            return 0