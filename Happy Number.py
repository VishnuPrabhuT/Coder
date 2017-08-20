class Solution(object):
    def calcSum(self,n):
        sum1=0
        while n:            
            digit=n%10
            n=n/10
            sum1+=digit**2
        if sum1==1:
                return True
        return sum1
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        follower=leader=n
        follower=self.calcSum(follower)
        leader=self.calcSum(self.calcSum(leader))
        if leader==1:
            return True
        while not(follower==leader):
            follower=self.calcSum(follower)
            leader=self.calcSum(self.calcSum(leader))
            if leader==1:
                return True
        return False
