# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tmp = head
        while tmp and tmp.next:
            temp = tmp.next
            if tmp.val == temp.val:
                tmp.next = temp.next
            else:
                tmp = tmp.next
        return head