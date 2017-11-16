class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result=[]
        for element in range(rowIndex+1):
            result.append(self.pascalElement(element,rowIndex))
        return result
    @staticmethod
    def pascalElement(element,row):
        return int(math.factorial(row)/(math.factorial(element)*math.factorial(row-element)))
