class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[0 for i in xrange(n)] for j in xrange(n)]
        for i in xrange(n):
            dp[i][i] = 1
        for curr_len in xrange(2, n+1):
            for i in xrange(0, n-curr_len+1):
                j = i + curr_len - 1
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][n-1]
