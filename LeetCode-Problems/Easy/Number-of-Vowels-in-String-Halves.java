//Java
class Solution {
    public boolean halvesAreAlike(String s) {
        String a = s.substring(0, s.length()/2).toLowerCase();
        String b = s.substring(s.length()/2).toLowerCase();
        char[] vowels = {'a', 'e', 'i', 'o', 'u'};
        int countA = 0;
        int countB = 0;
        
        for (int i = 0; i < a.length(); i++){
            for (int j = 0; j < vowels.length; j++){
                if (a.charAt(i) == vowels[j]){
                    countA++;
                }
                if (b.charAt(i) == vowels[j]){
                    countB++;
                }
            }
        }
        if (countA == countB){
            return true;
        }
        return false;
    }
}
