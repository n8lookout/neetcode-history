class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        answer = [0] * len(arr)
        rightMax = -1

        for i in range(len(arr) - 1, -1, -1):
            answer[i] = rightMax
            rightMax = max(rightMax, arr[i])

        return answer