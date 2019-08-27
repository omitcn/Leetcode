import json
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or head.next == None:
            return head
        nodeList = list()
        while head:
            nodeList.append(head)
            head = head.next
        i = 0
        while i < len(nodeList):
            if i + 3 < len(nodeList):
                nodeList[i].next = nodeList[i + 3]
                nodeList[i + 1].next = nodeList[i]
            elif i + 2 < len(nodeList):
                nodeList[i].next = nodeList[i + 2]
                nodeList[i + 1].next = nodeList[i]
            elif i + 1 < len(nodeList):
                nodeList[i].next = None
                nodeList[i + 1].next = nodeList[i]
            else:
                nodeList[i].next = None
            i += 2
        return nodeList[1]


def stringToIntegerList(input):
    return json.loads(input)


def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


def main():
    import sys
    import io

    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            head = stringToListNode(line)

            ret = Solution().swapPairs(head)

            out = listNodeToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
