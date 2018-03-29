# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n
        while low != high:
            mid = (low + high) / 2
            if not isBadVersion(mid):
                low = mid + 1
            else:
                high = mid
        return high
