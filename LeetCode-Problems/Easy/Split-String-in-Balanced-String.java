//Java
class Solution {
    public int balancedStringSplit(String s) {
        int count = 0;
        int balStr = 0;
        for (int i = 0; i < s.length(); i++){
            if (s.charAt(i) == 'L'){
                balStr++;
            }
            else{
                balStr--;
            }
            if (balStr == 0){
                count++;
            }
        }
        return count;
    }
}
