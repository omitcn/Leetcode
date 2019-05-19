from SolutionA import Solution
import re
S=Solution()
s = "qqq     +1234    344"
#s1 = (re.match('[\s]*[\+]?[\-]?\d+', s))
#s= s1.group() if s1!=None else 0
#print(s)
print(S.myAtoi(s))
