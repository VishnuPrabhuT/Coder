class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        def helper(nums, left, right, target):
            mid = (left + right)/2
            if left > right:
                return -1
            if nums[mid] == target:
                return mid
            return helper(nums, 0, mid-1, target) if target < nums[mid] else helper(nums, mid+1, right, target)
        return helper(nums, 0, len(nums)-1, target)
