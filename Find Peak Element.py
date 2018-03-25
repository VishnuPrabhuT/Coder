class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        slow, fast = 0, 1
        maxi = float('-inf')
        for i, val in enumerate(nums):
            curr = max(nums[slow], nums[fast])
            if curr > maxi:
                maxi = curr
                ret = slow if nums[slow] == maxi else fast
            slow, fast = slow+1, fast+slow
            fast = fast % len(nums) if fast >= len(nums) else fast
        return ret
