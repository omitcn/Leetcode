class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 2:
            return min(height) if height[0] != 0 and height != 0 else 0
        else:
            i = 0
            j = len(height) - 1
            maxV=0
            while j > i:
                if height[i] > height[j]:
                    maxV = maxV if maxV > (j - i) * height[j] else (j - i) * height[j]
                    j-= 1
                else:
                    maxV = maxV if maxV > (j - i) * height[i] else (j - i) * height[i]
                    i+= 1
            return maxV              