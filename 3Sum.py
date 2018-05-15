class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            start = i + 1
            end = len(nums) - 1
            while start < end:
                currSum = nums[i] + nums[start] + nums[end]
                if currSum < 0:
                    start += 1
                elif currSum > 0:
                    end -= 1
                else:
                    result.append([nums[i], nums[start], nums[end]])
                    currStart = start
                    while nums[start] == nums[currStart] and start < end:
                        start += 1
                    currEnd = end
                    while nums[end] == nums[currEnd] and start < end:
                        end -= 1
        return result
