
toSearch = [1, 3]


# approach
# it's still a sorted list, so we can do a binary search log(n) vs n
# need to find the original source (smallest #) and rebuild as a normally sorted array
# from there we can binary search as normal
class Solution(object):
    def findSmallest(self, nums):
        rangeStart = 0
        rangeEnd = len(nums) - 1

        while (rangeEnd > rangeStart):
            midPoint = int(rangeStart + ((rangeEnd - rangeStart) / 2))
            #print(rangeStart, midPoint, rangeEnd)
            if (nums[midPoint] < nums[rangeEnd]):
                # it's in first half
                rangeEnd = midPoint
            else:
                # it's in second half
                rangeStart = midPoint + 1
        
        return rangeStart

    def binarySearch(self, nums, target):
        rangeStart = 0
        rangeEnd = len(nums) - 1

        while (rangeEnd > rangeStart):
            midPoint = int(rangeStart + ((rangeEnd - rangeStart) / 2))
            #print(rangeStart, midPoint, rangeEnd)
            if (nums[midPoint] >= target):
                # it's in first half
                rangeEnd = midPoint
            else:
                # it's in second half
                rangeStart = midPoint + 1
        
        if (nums[rangeStart] == target):
            return rangeStart
        return -1

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        offset = 0
        location = -1

        if (len(nums) == 0):
            return -1
        if (len(nums) == 1 and nums[0] == target):
            return 0

        # find the index of the original first value to reset the array
        offset = self.findSmallest(nums)
        #print(offset)

        # slice and dice to original order, remembering offset for later
        orderedList = nums[offset:len(nums)]
        orderedList.extend(nums[0:(offset)])
        #print(orderedList)

        # try to find the target now that we have a sorted list
        location = self.binarySearch(orderedList, target)
        #print(location)
        if (location == -1):
            return -1

        
        if (target >= nums[0] and offset > 0):
            return location - (len(nums) - offset)
        return location + offset

print(Solution().search(toSearch, 1))