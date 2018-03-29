class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) / 2
            if ((nums[0] > target) ^ (nums[0] > nums[mid]) ^ (target > nums[mid])):
                low = mid + 1
            else:
                high = mid
        #print(nums[low:low+1])
        return low if target in nums[low:low+1] else -1
