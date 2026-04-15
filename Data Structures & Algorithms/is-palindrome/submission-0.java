class Solution {
    public boolean isPalindrome(String s) {
        char[] sChar = s.toCharArray();
        ArrayList<Character> newS = new ArrayList<>();
        
        for (int i = 0; i < sChar.length; i++){
            char fP = sChar[i];
            if (Character.isLetterOrDigit(fP)){
                newS.add(Character.toLowerCase(fP));
            }
        }

        for (int i = 0; i < newS.size() / 2; i++){
            char fP = newS.get(i);
            char sP = newS.get(newS.size() - 1 - i);

            if (fP != sP) {
                return false;
            }
        }
        return true;
    }
}
