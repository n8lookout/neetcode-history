class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> prevChecked = new HashSet<>();

        for (int i = 0; i < nums.length; i++){
            if (prevChecked.contains(nums[i])){
                return true;
            }
            prevChecked.add(nums[i]);
        }
        return false;
    }
}