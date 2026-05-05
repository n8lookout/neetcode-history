class Solution:
    def maxDepth(self, s: str) -> int:
        # Solution O(n) - time; O(1) - Space
        depth = 0
        maxDepth = 0
        
        for c in range(len(s)):
            # finding the open paren - going down in depth
            if s[c] == '(':
                depth += 1

            # finding the closed paren
            elif s[c] == ')':
                depth -= 1

            # always track the maximum depth
            maxDepth = max(maxDepth, depth)

        return maxDepth
