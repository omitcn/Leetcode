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
        if head and head.next:
            tmp=head.next
            temp=tmp.next
            head.next=None
            while temp:
                tmp.next=head
                head=tmp
                tmp=temp
                temp=temp.next
            tmp.next=head
            return tmp
        else:
            if head and head.next:
                tmp=head.next
                tmp.next=head
                head.next=None
                return tmp
            return head
                
                
        