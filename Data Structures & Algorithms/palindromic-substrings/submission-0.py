class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0

        for i in range(len(s)):
            left = right = i
            result += self.countPalindrome(s, left, right)
            
            left = i
            right = i + 1
            result += self.countPalindrome(s, left, right)
        return result
            
    def countPalindrome(self, s, left, right):
        result = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            result += 1
            left -= 1
            right += 1

        return result