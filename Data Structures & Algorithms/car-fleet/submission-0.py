class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[pos, spe] for pos, spe in zip(position, speed)]
        stack = []

        for pos, spe in sorted(pairs)[::-1]: # Reverse sorted order
            stack.append((target - pos) / spe)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)