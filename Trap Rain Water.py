class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right, res = 0, len(height) - 1, 0
        lMax, rMax = 0, 0
        while left < right:
            #print(height[left], height[right])
            if height[left] < height[right]:
                res = res + (lMax - height[left]) if height[left] < lMax else res
                lMax = max(height[left], lMax)
                left += 1
            else:
                res = res + (rMax - height[right]) if height[right] < rMax else res
                rMax = max(height[right], rMax)
                right -= 1
        return res
    
 ############################  Stack  #######################################

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stacky = []
        i, res = 0, 0
        while i < len(height):
            if not stacky or height[stacky[-1]] >= height[i]:
                stacky.append(i)
                i += 1
            else:
                top = stacky.pop()
                trap = 0 if not stacky else (min(height[i], height[stacky[-1]]) - height[top]) * (i-stacky[-1] - 1)
                res += trap
        return res
