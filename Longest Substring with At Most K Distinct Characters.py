class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        base = collections.defaultdict(int)
        maxlen = 0
        j = -1
        for i, c in enumerate(s):
            base[c] += 1
            while len(base) > k:
                j += 1
                base[s[j]] -= 1
                if base[s[j]] == 0:
                    del base[s[j]]
            maxlen = max(maxlen, i-j)
        return maxlen
