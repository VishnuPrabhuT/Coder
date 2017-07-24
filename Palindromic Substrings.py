class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        table=[[False for x in range(len(s))] for y in range(len(s))]
        n=len(s)
        count=0
        for i in range(n):
            table[i][i]=True
            if i+1<n:
                if s[i]==s[i+1]:
                    table[i][i+1]=True
            else:
                table[n-1][n-1]=True
        for step in range(3,n+1,1):
            for i in range(n-step+1):
                j=i+step-1
                if table[i+1][j-1]==True and s[i]==s[j]:
                    table[i][j]=True
        for i in range(len(table)):
            for j in range(len(table)):
                if table[i][j]==True:
                    count+=1
        return count
