# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None and l2 == None:
            return None
        elif (l1 == None and l2 != None) or (l1 != None and l2 == None):
            return l1 if l1 != None else l2
        elif l1 != None and l2 != None:
            if l1.val <= l2.val:
                temp = l1
                l1=l1.next
            else:
                temp = l2
                l2 = l2.next
            temp1 = temp
            while l1 != None and l2 != None:
                if l1.val <= l2.val:
                    temp1.next = l1
                    l1 = l1.next
                else:
                    temp1.next = l2
                    l2 = l2.next
                temp1 = temp1.next
            temp1.next = l1 if l1 != None else l2
            return temp
                
                
                
                
            
        