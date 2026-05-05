class Solution:
    def isValid(self, s: str) -> bool:
        # use stack for last in first out properties
        stack = []
        # use mapping for convenience
        mapping = {")": "(", "]": "[", "}": "{"}

        for char in s:
            # checking if it's a closing bracket
            if char in mapping:
                # ensure no dangling closing brace like "][]" and correct order
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:
                # if an open brack then push it to the stack
                stack.append(char)

        # ensures no trailing open braces like [](
        return len(stack) == 0
