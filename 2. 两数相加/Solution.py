# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = list()
        l4 = list()
        while l1 != None:
            l3.insert(0,l1.val)
            l1 = l1.next
        while l2 != None:
            l4.insert(0, l2.val)
            l2 = l2.next
        i = 0
        j = 0
        l5 = str()
        l6 = str()
        while i < len(l3):
            l5 = l5 + str(l3[i])
            i += 1
        while j < len(l4):
            l6 = l6 + str(l4[j])
            j += 1
        sum = int(l5) + int(l6)
        ll=list(map(int,str(sum)))
        l = ListNode(ll.pop())
        t=l
        while len(ll):
            t.next = ListNode(ll.pop())
            t = t.next
        return l
            
            