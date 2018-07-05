class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def swap(nums, i, j):
            tmp = nums[i] 
            nums [i] = nums[j]
            nums[j] = tmp
        for i in range(len(nums)):
            while nums[i] > 0 and nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]:
                swap(nums, i, nums[i]-1)
                print(nums)
        for i in range(len(nums)):
            if i+1 != nums[i]:
                return i+1
        return len(nums) + 1
