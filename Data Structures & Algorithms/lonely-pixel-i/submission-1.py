class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        ROWS, COLS = len(picture), len(picture[0])
        
        def is_isolated(row, col) -> bool:
            for i in range(COLS):
                if i == col:
                    continue
                elif picture[row][i] == 'B':
                    return False
            for i in range(ROWS):
                if i == row:
                    continue
                elif picture[i][col] == 'B':
                    return False
            return True

        result = 0;

        for r in range(ROWS):
            for c in range(COLS):
                if picture[r][c] == 'B' and is_isolated(r, c):
                    result += 1

        return result