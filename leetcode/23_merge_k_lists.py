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
1) iterate through; keeping track of smallest node and the reference to it
        after we reach end, pop it off
        n*m; we go through each list once per node we pop

2) think about various shortcuts
    -make a binary search tree out of these lists, organized by the first node in each list
        -then we can grab our node in log(m), n times
        -this costs us mlog(m) sorting time initially
            -worst case of nlog(m) popping + mlog(m) building the tree
            -so worst case is no worse than naive best case, because naive is forced to compare always
"""

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        result = None
        while (len(lists) > 0):
            i = 0
            smallestVal = None
            targetList = 0

            while (i < len(lists)):
                if (lists[i] != None): # only check the list if it isn't empty
                    currentNodeVal = lists[i].val
                    #print ("checking ", currentNodeVal)
                    if (smallestVal == None or currentNodeVal < smallestVal):
                        #print("new smallest: ", currentNodeVal)
                        targetList = i
                        smallestVal = currentNodeVal
                i = i + 1

            if (smallestVal != None):
                #print("now adding", smallestVal)
                lists[targetList] = lists[targetList].next
                newNode = ListNode(smallestVal)
                if (result == None):
                    result = newNode
                else:
                    tmp = result
                    while (tmp.next != None):
                        tmp = tmp.next
                    tmp.next = newNode
            else:
                lists = []
                # because of our inelegance in list management, we need to manually break

        return result
        

val = Solution().mergeKLists(listOfLists)
while (val != None):
    print(val.val)
    val = val.next

# expecting 1 3 4 5 7
