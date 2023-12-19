from Solution import ListNode
from Solution import Solution
l1 = ListNode(2)
t1 = l1
t1.next = ListNode(4)
t1 = t1.next
t1.next = ListNode(3)
l2 = ListNode(5)
t2 = l2
t2.next = ListNode(6)
t2 = t2.next
t2.next = ListNode(4)
sum = Solution()
print(sum.addTwoNumbers(l1,l2))
