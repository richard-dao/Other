//Java
class Solution {
    public int[] decode(int[] encoded, int first) {
        int[] decodedArray = new int[encoded.length+1];
        decodedArray[0] = first;
        int temp = 0;
        
        for(int i = 0; i < encoded.length; i++){
            temp = encoded[i] ^ decodedArray[i];
            decodedArray[i+1] = Math.abs(temp);
        }
        return decodedArray;
    }
}
