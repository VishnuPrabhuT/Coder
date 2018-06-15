class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        base = {}
        start, end, resStart = 0, 0, 0
        window = len(s) + 1
        count = len(t)
        for c in t:
            base[c] = base[c] + 1  if c in base else 1
        while end < len(s):
            if s[end] in base:
                if base[s[end]] > 0:
                    count -= 1
                base[s[end]] -= 1
            while count == 0:
                if end - start + 1 < window:
                    window = end - start + 1
                    resStart = start
                if s[start] in base:
                    base[s[start]] += 1
                    if base[s[start]] > 0:
                        count += 1
                start += 1
            end += 1
        return "" if window == len(s) + 1 else s[resStart : resStart+window]
