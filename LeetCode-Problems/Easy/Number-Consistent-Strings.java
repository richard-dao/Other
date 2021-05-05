//Java
class Solution {
    public int countConsistentStrings(String allowed, String[] words) {
        int count = 0;
        Set<String> allowedChars = new HashSet<String>();
        for (int i = 0; i < allowed.length(); i++){
            allowedChars.add(allowed.substring(i, i+1));
        }
        for (int i = 0; i < words.length; i++){
            boolean isConsistent = true;
            for (int j = 0; j < words[i].length(); j++){
                if (!(allowedChars.contains(words[i].substring(j, j+1)))){
                    isConsistent = false;
                    break;
                } 
            }
            if (isConsistent){
                count++;
            }
        }
        return count;
    }
}
