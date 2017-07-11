class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dicti={}
        for i in range(len(nums)):
            diff=target-nums[i]                      
            if nums[i] in dicti:
                return [dicti[nums[i]],i]
            else:
                dicti[diff]=i
                    
                
                    
            