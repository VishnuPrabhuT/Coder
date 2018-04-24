class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(haystack) < len(needle):
            return -1
        if not needle:
            return 0
        h, n = 0, 0
        while h < len(haystack) and n < len(needle):
            #print(haystack[h], needle[n])
            if haystack[h] != needle[n]:
                h = h - n + 1
                n = 0
                continue
            h += 1
            n += 1
        return h-n if n == len(needle) else -1
            
