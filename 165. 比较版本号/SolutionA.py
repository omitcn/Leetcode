class Solution:
    def compareVersion(self, version1, version2):
        v1=version1+'.0'*(3-version1.count('.'))
        v2=version2+'.0'*(3-version2.count('.'))
        v1=v1.split('.')
        v2.v2.split('.')
        for i,j in zip(v1,v2):
            if int(i) > int(j):
                return 1
            elif int(i) < int(j):
                return - 1
        return 0