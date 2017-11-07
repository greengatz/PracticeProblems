# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if (l1 == None or l2 == None):
            return l1 if l1 != None else l2

        if (l1.val < l2.val):
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        l2.next = self.mergeTwoLists(l1, l2.next)
        return l2


l1 = ListNode(4)
l1.next = ListNode(7)

l2 = ListNode(1)
l2.next = ListNode(5)

val = Solution().mergeTwoLists(l1, l2)
while (val != None):
    print(val.val)
    val = val.next