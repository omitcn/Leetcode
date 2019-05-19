# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        result = ListNode(0)
        result.next = head
        tmp = result
        while head:
            while n>1:
                head = head.next
                n = n - 1
            head = head.next
            temp=tmp
            tmp = tmp.next
        temp.next = tmp.next
        return result.next


            