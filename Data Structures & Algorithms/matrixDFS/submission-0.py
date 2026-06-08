class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(row, col) -> int:
            if(min(row, col) < 0 or col == COLS or row == ROWS or (row, col) in visited or grid[row][col] == 1):
                return 0
            if row == ROWS - 1 and col == COLS - 1:
                return 1

            visited.add((row, col))

            count = 0
            count += dfs(row + 1, col)
            count += dfs(row - 1, col)
            count += dfs(row, col + 1)
            count += dfs(row, col - 1)

            visited.remove((row, col))
            return count

        return dfs(0, 0)