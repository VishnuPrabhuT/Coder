class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n=len(s)        
        store=[[False for x in range(n)] for y in range(n)]  
        maxlen=0
        for i in range(n):            
            if i!=n-1:    
                if s[i]==s[i+1]:                    
                    store[i][i+1]=True
                    maxlen=2
                    start=i
                if s[i]==s[i]:
                    store[i][i]=True                    
            else:
                store[i][i]=True
                if maxlen==0:
                    start=i
                    maxlen=1        
        for step in range(3,n+1,1):
            #print(step)
            for i in range(n-step+1):
                j=i+step-1
                #print(j)
                if store[i+1][j-1]==True and s[i]==s[j]:
                    store[i][j]=True                    
                    if(step>maxlen):
                        maxlen=step
                        start=i                                
        return s[start:start+maxlen]
            
