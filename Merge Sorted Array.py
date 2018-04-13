class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        ins = m+n-1
        while n > 0:
            if m <=0 or nums1[m-1] <= nums2[n-1]:
                nums1[ins] = nums2[n-1]
                n -= 1
            else:
                nums1[ins] = nums1[m-1]
                m -= 1
            ins -= 1
