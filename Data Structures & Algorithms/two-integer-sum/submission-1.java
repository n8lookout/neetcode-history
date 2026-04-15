class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Map to check again - uses numbers in array as the key and the index of those numbers are the values
        Map<Integer, Integer> prev = new HashMap<>();

        for (int i = 0; i < nums.length; i++){
            // Calculate the Difference
            int diff = target - nums[i];
            if (prev.containsKey(diff)){
                return new int[]{prev.get(diff), i};
            }
            prev.put(nums[i], i);
        }
        return null;
    }
}
