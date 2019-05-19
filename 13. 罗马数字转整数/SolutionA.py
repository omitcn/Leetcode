class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum=0
        switch={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        i=0
        while i<len(s):
            if i+1<len(s) and switch[s[i]]>=switch[s[i+1]]:
                sum=sum+switch[s[i]]
                i+=1
            elif i+1<len(s) and switch[s[i]]<switch[s[i+1]]:
                sum=sum+switch[s[i+1]]-switch[s[i]]
                i=i+2
            elif i+1==len(s):
                sum=sum+switch[s[i]]
                i+=1
        return sum





            
