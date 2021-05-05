//Java
class Solution {
    public String defangIPaddr(String address) {
        String returnedString = "";
        for (int i = 0; i < address.length(); i++){
            if (address.substring(i, i+1).equals(".")){
                returnedString += "[.]";
            }
            else{
                returnedString += address.substring(i,i+1);
            }
        }
        return returnedString;
    }
}
