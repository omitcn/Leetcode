class Solution:
    def compress(self, chars):
        i, j = 0, 0
        c_len = len(chars)
        while i < c_len and j < c_len:
            k = i + 1
            tmp=1
            while k < c_len and chars[k] == chars[i]:
                tmp += 1
                k += 1
            if tmp > 9:
                temp = list(str(tmp))
                for x in temp:
                    chars[j + 1] = x
                    j += 1
                j += 1
                if k < c_len:
                    chars[j] = chars[k]
            elif tmp > 1:
                chars[j + 1] = str(tmp)
                if k < c_len:
                    chars[j + 2] = chars[k]
                    j += 2
                else:
                    return j + 2                
            else:
                j += 1
                if k < c_len:
                    chars[j] = chars[k]
            i = k
        return j
        