# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        qlist=list()
        while head:
            qlist.append(head)
            head=head.next
        i=len(qlist)-1
        while i>0:
            qlist[i].next=qlist[i-1]
            i-=1
        qlist[0].next=None
        return qlist.pop()
        