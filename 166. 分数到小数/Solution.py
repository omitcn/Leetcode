class Solution:
    def fractionToDecimal(self, numerator, denominator):
        if not numerator % denominator:
            return str(numerator // denominator)
        if numerator * denominator > 0:
            flag = 0
        else:
            flag = 1
            numerator, denominator = abs(numerator), abs(denominator)
        list_residue, list_quotient = [numerator % denominator], [numerator // denominator]
        list_quotient.append('.')
        numerator = list_residue[-1] * 10
        quotient, residue = numerator // denominator, numerator % denominator
        while residue and residue not in list_residue:
            list_quotient.append(quotient)
            list_residue.append(residue)
            numerator = residue * 10
            quotient, residue = numerator // denominator, numerator % denominator
        list_quotient.append(quotient)
        if not residue:
            res = ''.join([str(x) for x in list_quotient])
            return res if not flag else '-' + res
        else:
            index = list_residue.index(residue)
            res = ''.join(str(x) for x in list_quotient[: index + 2]) + '(' + ''.join([str(x) for x in list_quotient[index + 2 :]])+')'
            return res if not flag else '-' + res