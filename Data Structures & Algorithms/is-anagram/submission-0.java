class Solution {
    public boolean isAnagram(String s, String t) {
        // Return false if lengths are different
        if (s.length() != t.length()){
            return false;
        }

        // Convert to character arrays
        char[] charS = s.toCharArray();
        char[] charT = t.toCharArray();

        // Sort
        Arrays.sort(charS);
        Arrays.sort(charT);

        // Compare
        return Arrays.equals(charS, charT);
    }
}
