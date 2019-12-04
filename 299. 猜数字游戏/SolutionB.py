class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        from collections import Counter
        s_c = Counter(secret)
        g_c = Counter(guess)
        t = sum(i == j for i, j in zip(secret, guess))
        return "{}A{}B".format(t, sum((s_c & g_c).values()) - t)


'''
作者：powcai
链接：https://leetcode-cn.com/problems/bulls-and-cows/solution/pythonde-counter-by-powcai/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
