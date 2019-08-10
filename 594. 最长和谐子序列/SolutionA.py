from __future__ import annotations
from collections import Counter


class Solution:
    def findLHS(self, nums) -> int:
        dic_nums = Counter(nums)
        res = 0
        for key in dic_nums:
            if dic_nums[key + 1] in dic_nums:
                res = max(res, dic_nums[key] + dic_nums[key + 1])
        return res
