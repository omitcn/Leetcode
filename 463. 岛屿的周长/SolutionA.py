class Solution:
    def islandPerimeter(self, grid):
        if not grid:
            return 0
        row, col = len(grid), len(grid[0])
        res = 0
        for i in range(row):
            for j in range(col):
                l, r, u, d = j - 1, j + 1, i - 1, i + 1
                if grid[i][j]:
                    if l<0 or grid[i][l] == 0:
                        res += 1
                    if r >= col or grid[i][r] == 0:
                        res += 1
                    if u < 0 or grid[u][j] == 0:
                        res += 1
                    if d >= row or grid[d][j] == 0:
                        res += 1
        return res