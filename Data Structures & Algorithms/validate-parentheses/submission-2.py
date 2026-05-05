class Solution:
    def isValid(self, s: str) -> bool:
        # use stack for last in first out properties
        stack = []
        # use mapping for convenience
        mapping = {")": "(", "]": "[", "}": "{"}
        open_bracket_set = {"(", "[", "{"}

        for char in s:
            # checking if it's a closing bracket
            if char in mapping:
                # ensure no dangling closing brace like "][]" and correct order
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:
                # if an open brack then push it to the stack
                if char in open_bracket_set:
                    stack.append(char)

        # ensures no trailing open braces like [](
        return len(stack) == 0
