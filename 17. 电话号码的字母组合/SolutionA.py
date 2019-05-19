import itertools
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        l_map = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', 
                 '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        
        chars = [l_map.get(d) for d in digits]
        return [''.join(x) for x in itertools.product(*chars)]
'''
--------------------- 
作者：coordinate_blog 
来源：CSDN 
原文：https://blog.csdn.net/qq_17550379/article/details/82459849 
版权声明：本文为博主原创文章，转载请附上博文链接！
'''