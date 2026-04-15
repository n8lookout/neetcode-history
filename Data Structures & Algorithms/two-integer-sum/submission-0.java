class Solution {
    public int[] twoSum(int[] nums, int target) {        
        // Previous checked values to index
        Map<Integer, Integer> checkedValuesMap = new HashMap<>();

        for (int i = 0; i < nums.length; i++){
            int difference = target - nums[i];
            if (checkedValuesMap.containsKey(difference)){
                return new int[]{checkedValuesMap.get(difference), i};
            }
            checkedValuesMap.put(nums[i], i);
        }
        return null;
    }
}
