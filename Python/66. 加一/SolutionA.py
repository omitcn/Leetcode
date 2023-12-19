class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        dlen = len(digits)-1
        if digits[dlen] + 1 < 10:
            digits[dlen] += 1
            return digits
        else:
            i = dlen
            digits[dlen] += 1
            while i >=1 and digits[i] == 10:
                digits[i] = 0
                i -= 1
                digits[i] += 1
            if digits[0] < 10:
                return digits
            else:
                digits[0] = 0
                digits.insert(0, 1)
                return digits
