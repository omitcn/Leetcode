class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        while None in lists:
            lists.remove(None)
        if not lists:
            return None
        print(lists)
        i = 0
        res = []
        while i < len(lists):
            node = lists[i]
            while node:
                res.append(node)
                node = node.next
            i += 1
        res.sort(key=lambda ele: ele.val)
        for i in range(len(res) - 1):
            res[i].next = res[i + 1]
        res[len(res) - 1].next = None
        return res[0]
