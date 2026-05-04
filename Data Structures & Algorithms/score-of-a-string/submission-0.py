class Solution:
    def scoreOfString(self, s: str) -> int:
        result = 0

        for i in range(len(s) - 1):
            c1 = s[i]
            c2 = s[i + 1]

            result += abs(ord(c1) - ord(c2))
        return result
