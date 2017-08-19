class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """        
        if n<=2:
            return n
        else:
            return self.findWays(0,1,1,n)
    def findWays(self,prev,curr,i,n):        
        temp=prev
        prev=curr
        curr=temp+curr        
        if i<n:
            curr=self.findWays(prev,curr,i+1,n)                    
        return curr
