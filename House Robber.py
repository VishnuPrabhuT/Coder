class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum1=0
        sum2=0
        curr=0
        for i in nums:
            curr=sum1
            sum1=max(i+sum2,sum1)
            sum2=curr
        return sum1
