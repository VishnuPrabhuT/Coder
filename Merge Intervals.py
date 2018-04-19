# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        ret = []
        intervals.sort(key = lambda x: x.start)
        for interval in intervals:
            if not ret or ret[-1].end < interval.start:
                ret.append(interval)
            else:
                ret[-1].end = max(interval.end, ret[-1].end)
        return ret
