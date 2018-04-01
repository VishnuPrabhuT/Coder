class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        def helpMe(nums, target, left):
            low, high = 0, len(nums)
            while low < high:
                mid = (low + high) / 2
                #print((nums[mid] > target) or (left and target == nums[mid]), nums[mid])
                if (nums[mid] > target) or (left and target == nums[mid]):
                    high = mid
                else:
                    low = mid + 1
            return low
        l = helpMe(nums, target, True)
        if l == len(nums) or nums[l] != target:
            return [-1, -1]
        return [l, helpMe(nums, target, False) - 1]
