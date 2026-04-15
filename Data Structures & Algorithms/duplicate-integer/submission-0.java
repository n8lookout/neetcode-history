class Solution {
    public boolean hasDuplicate(int[] nums) {      
        // Create map
        Map<Integer, Integer> uniqueNums = new HashMap<>();

        // Loop through array adding each items to the map after checking to see if the item is already in the map
        for (int i = 0; i < nums.length; i++){
            if (!uniqueNums.containsValue(nums[i])){
                uniqueNums.put(i, nums[i]);
            }
        }

        // Return the comparison between the map length and the original array length
        return !(nums.length == uniqueNums.size());
    }
}