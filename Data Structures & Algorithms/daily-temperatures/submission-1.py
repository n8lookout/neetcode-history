class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        N = len(temperatures)
        result = [0] * N
        index_stack = []

        for i in range(N):
            # Pop Conditions
            while index_stack and temperatures[i] > temperatures[index_stack[-1]]:
                prev_index = index_stack.pop()
                result[prev_index] = i - prev_index
            # Push Conditions            
            index_stack.append(i)

        return result