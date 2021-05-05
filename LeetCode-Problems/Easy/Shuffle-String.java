//Java
class Solution {
    public String restoreString(String s, int[] indices) {
        String returnedString = "";
        for (int i = 0; i < indices.length; i++){
            for (int j = 0; j < indices.length; j++){
                if (indices[j] == i){
                    returnedString += s.substring(j, j+1);
                }
            }
        }
        return returnedString;
        
    }
}
