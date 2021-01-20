# DFS
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or len(grid) == 0:
            return 0
        
        islands = 0
        for i in range(len(grid)): # Rows
            for j in range(len(grid[0])): # Columns
                if grid[i][j] == '1': # If location in grid is marked as an Island
                    islands += 1
                    self.partOfIslands(i,j,grid) # Use DFS to find if it has any other islands connected to it   
        return islands
    
    # This performs recursion starting from a singular point and does a depth first search on all the points around it
    def partOfIslands(self, i, j, grid):
        if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '0'
        self.partOfIslands(i,j+1, grid)
        self.partOfIslands(i,j-1,grid)
        self.partOfIslands(i+1,j,grid)
        self.partOfIslands(i-1,j,grid)