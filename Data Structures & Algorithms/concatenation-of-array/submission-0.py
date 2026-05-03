class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result = []
        newLength = len(nums) * 2

        for i in range(newLength):
            if i < len(nums):
                result.append(nums[i])
            else:
                result.append(nums[i - len(nums)])

        return result