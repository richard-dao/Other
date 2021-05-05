//Java
class Solution {
    public boolean arrayStringsAreEqual(String[] word1, String[] word2) {
        String catWord1 = "";
        String catWord2 = "";
        for (int i = 0; i < word1.length; i++){
            catWord1 += word1[i];
        }
        for (int i = 0; i < word2.length; i++){
            catWord2 += word2[i];
        }
        if (catWord1.equals(catWord2)){
            return true;
        }
        else{
            return false;
        }
    }
}
