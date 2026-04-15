class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> result = new HashMap<>();
        // 1. Iterate through the array
        // 2. Convert each string into a sorted character array - will replicate for any word with the same characters
        // 3. Create a string with the sorted character array
        // 4. Use putIfAbsent to check if the key is there
        // 5. Add string as value to the key of the sorted string
        // 6. End by returning a new list created from the values of each key in the map, which are lists of strings.
        for (String string : strs){
            char[] charAr = string.toCharArray();
            Arrays.sort(charAr);
            String sortedString = new String(charAr);
            result.putIfAbsent(sortedString, new ArrayList<>());
            result.get(sortedString).add(string);
        }

        return new ArrayList<>(result.values());
    }
}