import Math
def minPathSum(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    x = len(grid)
    y = len(grid[0])
    for i in range(x-1):
        grid[x-i-2][y-1] += grid[x-i-1][y-1]
    for i in range(y-1):
        grid[x-1][y-i-2] += grid[x-1][y-i-1]
    
    for i in range(x-1):
        for j in range(y-1):
            grid[x-i-2][y-j-2] += min(grid[x-i-1][y-j-2],grid[x-i-2][y-j-1])

    return grid[0][0]
