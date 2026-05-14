class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        unique_nums = set()
        result = -1

        for i in range(len(nums)):
            if nums[i] in unique_nums:
                result = nums[i]
            else:
                unique_nums.add(nums[i])

        return result