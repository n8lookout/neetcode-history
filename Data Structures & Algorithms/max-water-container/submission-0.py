class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxArea = 0

        while left < right:
            tmpWidth = right - left
            tmpHeight = min(heights[left], heights[right])
            tmpArea = tmpWidth * tmpHeight

            maxArea = max(maxArea, tmpArea)

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1

        return maxArea