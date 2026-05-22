class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        freq_map = Counter(nums)

        return max(
            (num for num, freq in freq_map.items() if freq == 1), 
            default = -1)