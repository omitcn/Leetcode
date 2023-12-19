#排名最高的算法##表示没看懂题目#
class Solution:
    def countAndSay(self, n: 'int') -> 'str':
        # solution 1
        ans, nums = '1', []
        for _ in range(1, n):
            n = len(ans)
            cnt, pre = 1, ans[0]
            for i in range(1, len(ans)):
                if ans[i] == pre:
                    cnt += 1
                else:
                    nums.append('{}{}'.format(cnt, pre))
                    cnt, pre = 1, ans[i]
            else:
                nums.append('{}{}'.format(cnt, pre))
            ans = ''.join(nums)
            nums.clear()
        return ans