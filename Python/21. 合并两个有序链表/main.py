from SolutionA import ListNode
from SolutionA import Solution
l1 = ListNode("a")
l1.next = ListNode("b")
temp = l1
temp.next = ListNode("c")
print(l1.next.val)