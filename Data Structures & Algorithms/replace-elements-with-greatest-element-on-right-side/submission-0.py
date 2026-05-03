class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            maxRight = float('-inf')
            for j in range(i + 1, len(arr)):
                maxRight = max(maxRight, arr[j])
            arr[i] = maxRight
            if i == len(arr) - 1:
                arr[i] = -1

        return arr