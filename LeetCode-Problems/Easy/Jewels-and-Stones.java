//Java
class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        int count = 0;
        for (int i = 0; i < stones.length(); i++){
            for (int j = 0; j < jewels.length(); j++){
                if (jewels.substring(j, j+1).equals(stones.substring(i, i+1))){
                    count++;
                }
            }
        }
        return count;
    }
}
