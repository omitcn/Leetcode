class Solution:
    def __init__(self):
        self.res = ''
    def tree2str(self, t):
        if not t:
            return ''
        self.res += str(t.val)
        if t.left and not t.right:
            self.res += '('
            self.tree2str(t.left)
            self.res += ')'
        elif not t.left and t.right:
            self.res += '()('
            self.tree2str(t.right)
            self.res += ')'
        elif t.left and t.right:
            self.res += '('
            self.tree2str(t.left)
            self.res += ')('
            self.tree2str(t.right)
            self.res += ')'
        return self.res