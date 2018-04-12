class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret, place = 0, 0
        for index, c in enumerate(list(s)):
            
            ret = ret * 26 + ((ord(s[index]) - ord('A')) + 1)
        return ret
