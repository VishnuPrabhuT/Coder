class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic=[]
        counter=0
        max=0
        for c in s:
            if c not in dic:                
                dic.append(c)
                counter+=1
                if counter>max:
                    max=counter
            else:
                dic=dic[dic.index(c)+1:]
                
                dic.append(c)
                counter=len(dic);
        return max
