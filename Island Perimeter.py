class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ret = 0
        for rI in range(len(grid)):
            for cI in range(len(grid[0])):
                if grid[rI][cI] == 1:
                    if cI-1 < 0 or grid[rI][cI-1] == 0:
                        ret += 1
                    if cI+1 >= len(grid[0]) or grid[rI][cI+1] == 0:
                        ret += 1
                    if rI-1 < 0 or grid[rI-1][cI] == 0:
                        ret += 1
                    if rI+1 >= len(grid) or grid[rI+1][cI] == 0:
                        ret += 1
        return ret
