class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length == 0){
            return 0;
        }
        Set<Integer> set = Arrays.stream(nums)
                         .boxed()
                         .collect(Collectors.toSet());
        int longest = 0;
        int length = 0;


        for (int i = 0; i < nums.length; i++){
            if (!set.contains(nums[i] - 1)){
                while (set.contains(nums[i] + length)){
                    length++;
                }
                longest = Math.max(length, longest);
                length = 0;
            }
        }     

        return longest;
    }
}
