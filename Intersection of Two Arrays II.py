class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        freq = {}
        res = []
        for i in nums1:
            freq[i] = 1 if i not in freq else freq[i] + 1
        for i in nums2:
            if i in freq and freq[i] > 0:
                res.append(i)
                freq[i] -= 1
        return res
