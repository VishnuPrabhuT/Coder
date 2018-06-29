class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maxy = 0
        count = [0]
        def sink(i, j, count):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return 0
            count[0] += 1
            grid[i][j] = 0
            sink(i+1, j, count)
            sink(i-1, j, count)
            sink(i, j+1, count)
            sink(i, j-1, count)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count[0] = 0
                    sink(i, j, count)
                    maxy = max(maxy, count[0])
        return maxy
