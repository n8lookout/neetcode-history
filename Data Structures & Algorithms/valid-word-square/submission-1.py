class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        ROWS, COLS = len(words), len(words[0])
        if ROWS != COLS:
            return False

        for row in range(len(words)):
            for col in range(len(words[row])):
                if col >= len(words) or \
                    row >= len(words[col]) or \
                    words[row][col] != words[col][row]:
                    return False

        return True