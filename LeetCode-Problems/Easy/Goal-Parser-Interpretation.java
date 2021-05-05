//Java
class Solution {
    public String interpret(String command) {
        String returnedString = "";
        for (int i = 0; i < command.length(); i++){
            if (command.substring(i, i+1).equals("G")){
                returnedString += "G";
            }
            if (i < command.length()-1){
                if (command.substring(i, i+2).equals("()")){
                    returnedString += "o";
                }
            }
            if (i < command.length()-3){
                if (command.substring(i, i+4).equals("(al)")){
                    returnedString += "al";
                }
            }
        }
        return returnedString;
    }
}
