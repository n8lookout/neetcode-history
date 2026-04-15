class Solution {
    public boolean hasDuplicate(int[] nums) {
        Map prevChecked = new HashMap<>();

        for (int i = 0; i < nums.length; i++){
            if (prevChecked.containsValue(nums[i])){
                return true;
            }
            prevChecked.put(i, nums[i]);
        }
        return false;
    }
}