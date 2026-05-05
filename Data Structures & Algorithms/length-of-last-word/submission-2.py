class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i, result = len(s) - 1, 0

        while s[i] == ' ':
            i -= 1
        while i >= 0 and s[i] != ' ':
            i -= 1
            result += 1
        return result
            