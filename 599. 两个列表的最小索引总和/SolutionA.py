class Solution:
    def findRestaurant(self, list1, list2):
        set1 = set.intersection(set(list1), set(list2))
        tmp = dict()
        res = list()
        for item in set1:
            tmp[item] = list1.index(item) + list2.index(item)
        temp = sorted(tmp.items(), key=lambda x: x[1])
        res.append(temp[0][0])
        for i in range(1,len(temp)):
            if temp[i][1] == temp[0][1]:
                res.append(temp[i][0])
        return res