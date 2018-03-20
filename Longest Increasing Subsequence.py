class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tails = [0] * len(nums)
        size, mid = 0, 0
        for num in nums:
            i, j = 0, size
            while i != j:
                #print(tails, num, i, j, "mid - " + str(mid))
                mid = (i + j)/2
                if tails[mid] < num:
                   i = mid + 1 
                else:
                    j = mid
            tails[i] = num
            size = max(i+1, size)
            #print(tails)
        return size
