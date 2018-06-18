class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        if not nums1:
            nums1 = nums2
        low, high = 0, len(nums1)
        x, y = len(nums1), len(nums2)
        while low <= high:
            ptrX = (low + high) / 2
            ptrY = (x + y + 1) / 2 - ptrX
            maxLeftX = float('-inf') if ptrX == 0 else nums1[ptrX - 1]
            minRightX = float('inf') if ptrX == x else nums1[ptrX]
            #print(ptrX, ptrY)
            maxLeftY = float('-inf') if ptrY == 0 else nums2[ptrY - 1]
            minRightY = float('inf') if ptrY == y else nums2[ptrY]
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if not (x + y) % 2:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
                else:
                    return float(max(maxLeftX, maxLeftY))
            elif maxLeftX > minRightY:
                high = ptrX - 1
            else:
                low = ptrX + 1
        return -1
