class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        memo = [0] * len(s)
        for word in dict:
            pos = s.find(word)
            while pos != -1:
                memo[pos:pos+len(word)] = [1] * len(word)
                pos = s.find(word, pos+1)
        temp = []
        for i in range(len(s)):
            if memo[i] and (i ==0 or not memo[i-1]):
                temp.append("<b>")
            temp.append(s[i])
            if memo[i] and (i == len(s)-1 or not memo[i+1]):
                temp.append("</b>")
        return ''.join(temp)
