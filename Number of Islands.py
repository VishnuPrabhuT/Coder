class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def sink(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == "0":
                return 0
            grid[i][j] = "0"
            sink(i+1, j)
            sink(i-1, j)
            sink(i, j+1)
            sink(i, j-1)
            return 1
        return sum(sink(i,j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == "1")
