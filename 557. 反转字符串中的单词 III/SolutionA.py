class Solution:
    def reverseWords(self, s):
        l = s.split()
        l_len = len(l)
        for i in range(l_len):
            l[i] = l[i][::-1]
        return ' '.join(l)
        