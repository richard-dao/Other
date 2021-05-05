//Java
class Solution {
    public String toLowerCase(String str) {
        int selected;
        String rString = "";
        for (int i = 0; i < str.length(); i++){
            selected = (int) str.charAt(i);
            if (selected < 91 && selected >= 65){
                rString += (char) (selected + 32);
            }
            else{
                rString += (char) selected;
            } 
        }
        return rString;
    }
}
