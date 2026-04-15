class Solution {

    public String encode(List<String> strs) {
        String result = new String();
        String delimit = "#";

        for (String string : strs){
            int length = string.length();
            String encode = String.valueOf(length) + delimit + string;
            result += encode;
        }

        return result;
    }

    public List<String> decode(String str) {
        List<String> result = new ArrayList<>();
        
        int i = 0;        
        while (i < str.length()) {
            // 1. Find the delimiter '#'
            int j = str.indexOf('#', i); 
        
            // 2. Parse the FULL length (handles "10#...", not just "1#...")
            int len = Integer.parseInt(str.substring(i, j));
        
            // 3. Extract the string starting AFTER the '#'
            int start = j + 1;
            int end = start + len;
            result.add(str.substring(start, end));
        
            // 4. Update 'i' to the start of the next segment
            i = end;
        }   
        
        return result;
    }
}
