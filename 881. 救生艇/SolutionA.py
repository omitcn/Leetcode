class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        i, j = 0, len(people)-1
        res = 0
        while i < j:
            if people[i]+people[j] <= limit:
                res += 1
                i += 1
                j -= 1
            else:
                res += 1
                i += 1
            if i == j:
                res += 1
        return res
