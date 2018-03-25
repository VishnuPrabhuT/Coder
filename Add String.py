class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        p1, p2 = len(num1)-1, len(num2)-1
        ret, s = [], 0
        while p1 > -1 or p2 > -1 or s:
            n1 = int(num1[p1]) if p1 > -1 else 0
            n2 = int(num2[p2]) if p2 > -1 else 0
            s = n1 + n2 + s
            d = s % 10
            s /= 10
            p1 -= 1
            p2 -= 1
            ret.extend([str(d)])
        return ''.join(ret[::-1])
            
        
