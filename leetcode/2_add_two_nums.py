# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


"""
wrong way to think about it, trying to do iterative math
let the language do the actual lifting
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        result = None
        lastResult = None
        while (l1 != None):
            tmp = l1.val + l2.val + carry
            if (tmp > 9):
                carry = 1
                tmp = tmp - 10
            else:
                carry = 0

            resNode = ListNode(tmp)
            if (result == None):
                result = resNode
                lastResult = resNode
            else:
                lastResult.next=resNode
                lastResult = resNode

            l1 = l1.next
            l2 = l2.next
        return result
"""

class Solution(object):
    def expandNum(self, l1):
        runningNum = 0
        runningMult = 1
        while (l1 != None):
            runningNum = runningNum + runningMult * l1.val
            runningMult = runningMult * 10
            l1 = l1.next
        return runningNum

    def collapseNum(self, number):
        root = None
        lastNode = None
        while (number > 0 or root == None):
            currentOnes = number % 10
            number = int((number - currentOnes) / 10)
            currentNode = ListNode(currentOnes)
            if (root == None):
                root = currentNode
            else:
                lastNode.next = currentNode
            lastNode = currentNode
        return root

    def addTwoNumbers(self, l1, l2):
        ex1 = self.expandNum(l1)
        ex2 = self.expandNum(l2)
        return self.collapseNum(ex1 + ex2)

val = Solution2().addTwoNumbers(l1, l2)
while (val != None):
    print(val.val)
    val = val.next
