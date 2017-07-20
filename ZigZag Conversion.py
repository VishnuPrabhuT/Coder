class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        st=['' for x in range(numRows)]
        row=numRows        
        direction='down'
        row=0
        for c in s:
            if row==0:
                direction='down'
                st[row]+=c
                row+=1
            elif row>0 and row<numRows-1:                
                st[row]+=c
                if direction=='up':
                    row-=1
                elif direction=='down':
                    row+=1
            elif row==numRows-1:
                direction='up'
                st[row]+=c
                row-=1            
        res=''
        if numRows==1:
            return s;
        for coll in st:
            res+=coll
        return res
