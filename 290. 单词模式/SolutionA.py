class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        list1=str.split()
        if len(list1)!=len(pattern):
            return False
        return len(set(zip(pattern,list1)))==len(set(list(pattern)))==len(set(str.split()))
                