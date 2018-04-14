class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        res = []
        for i in num:
            while res and k and res[-1] > i:
                k -= 1
                res.pop()
            res.append(i)
        return ''.join(res[:-k or None]).lstrip('0') or "0"
