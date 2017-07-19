class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
            flag=-1
        elif x>=0:
            flag=1
        numStr=str(x);
        revStr=numStr[::-1]
        if flag<0:
            revStr=revStr.replace('-','')
            revStr='-'+revStr
        if int(revStr)<=2**31-1 and int(revStr)>=-2**31-1:
            return int(revStr)
        else:
            return 0
