# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

l1 = ListNode(4)
l1.next = ListNode(7)

l2 = ListNode(1)

l3 = ListNode(3)
l3.next = ListNode(5)
l3.next.next = ListNode(8)

listOfLists = [l1, l2, l3]

"""
listOfLists = ListNode(l1)
listOfLists.next = ListNode(l2)
listOfLists.next.next = ListNode(l3)
"""

"""
approach:
well then, I way overthought this one. 1st approach was comparing against all other lists,
but that gives a worst case of n^2 (all lists one node). If we just take it all, put it in a list,
sort, and pop, we get ourselves nlogn worst case.
"""

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        allNodes = []

        # put all values in a lists
        for i in range(len(lists)):
            currentList = lists[i]
            while (currentList != None):
                allNodes.append(currentList.val)
                currentList = currentList.next

        # sort the list
        allNodes = sorted(allNodes)

        # make that our linked list to return
        result = None
        for i in reversed(range(len(allNodes))):
            currentNode = ListNode(allNodes[i])
            currentNode.next = result
            result = currentNode

        return result
        

val = Solution().mergeKLists(listOfLists)
while (val != None):
    print(val.val)
    val = val.next

# expecting 1 3 4 5 7
