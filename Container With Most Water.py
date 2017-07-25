class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea=0
        maxHeight=0
        currHeight=0
        area=0
        start=0
        end=len(height)-1
        while start<end:
            print(end)
            if height[start]<height[end]:
                area=height[start]*(end-start)
                start=start+1
            else:
                area=height[end]*(end-start)
                end=end-1            
            if maxArea<area:
                maxArea=area                
        return maxArea
