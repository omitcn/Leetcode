s = [1, 2, 2, 3, 4, 5, 5, 5, 5, 5, 5, 6, 7, 7, 7, 7, 7, 8]
i=0
while i < len(s):
    if i + 1 < len(s) and s[i] == s[i + 1]:
        del s[i + 1]
        continue
    i=i+1
print(s)
    