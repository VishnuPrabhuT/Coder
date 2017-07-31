class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs==[] or "" in strs:
            return ""
        for i,x in enumerate(zip(*strs)):
            if len(set(x))>1:
                print(strs)
                return strs[0][:i]
        else:
            print(strs)
            return min(strs)
