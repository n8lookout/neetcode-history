class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> countedValues = new HashMap<>();
        int[] result = new int[k];

        for (int i = 0; i < nums.length; i++){
            countedValues.put(nums[i], countedValues.getOrDefault(nums[i], 0) + 1);
        }

        List<int[]> array = new ArrayList<>();
        for (Map.Entry<Integer, Integer> entry : countedValues.entrySet()){
            array.add(new int[] {entry.getValue(), entry.getKey()});
        }

        array.sort((a, b) -> b[0] - a[0]);

        for (int i = 0; i < k; i++){
            result[i] = array.get(i)[1];
        }

        return result;
    }
}
