class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        result = max_count = 0

        for num in nums:
            count[num] += 1
            if max_count < count[num]:
                result = num
                max_count = count[num]

        return result