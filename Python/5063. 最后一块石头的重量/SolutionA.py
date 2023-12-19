from __future__ import annotations
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort(reverse=True)
        i = 1
        while i < len(stones):
            stones[0], stones[1] = abs(stones[0] - stones[1]), 0
            stones.sort(reverse=True)
            i += 1
        return stones[0]