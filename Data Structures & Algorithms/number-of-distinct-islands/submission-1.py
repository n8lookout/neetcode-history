class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        # Define dfs
        def dfs(r, c):
            # Hitting water condition
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or not grid[r][c]:
                return
            # What we're going to do if it's land - Check if seen, enter into our current
            if (r, c) in seen:
                return

            seen.add((r, c))
            # Normalize the points
            current_island.add((r - row_origin, c - col_origin))

            # Recursively call dfs
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        seen = set()
        unique_islands = set()

        for r in range(ROWS):
            for c in range(COLS):
                current_island = set()
                row_origin = r
                col_origin = c
                dfs(r, c)
                # Ensures that we don't add an empty set
                if current_island:
                    unique_islands.add(frozenset(current_island))

        return len(unique_islands)