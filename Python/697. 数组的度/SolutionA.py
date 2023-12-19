from __future__ import annotations
from collections import Counter


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        word_counts = Counter(nums)
        top = word_counts.most_common()
        for i in range(1, len(top)):
            if top[i][1] < top[i - 1][1]:
                top = top[:i]
                break
        res = []
        for items in top:
            i = nums.index(items[0])
            j = len(nums) - (nums[::-1]).index(items[0])
            res.append(j-i)
        return min(res)
