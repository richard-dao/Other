//Java
import java.util.ArrayList;
class Solution {
    public int uniqueMorseRepresentations(String[] words) {
        String[] morse = {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
        String[] transforms = new String[words.length];
        ArrayList<String> differents = new ArrayList<String>();
        int count = 0;
        for (int i = 0; i < words.length; i++){
            String conversion = "";
            for (int j = 0; j < words[i].length(); j++){
                int asciiLetter = (int) words[i].charAt(j);
                asciiLetter = asciiLetter - 97;
                conversion += morse[asciiLetter];
            }
            transforms[i] = conversion;
        }
        
        for (int i = 0; i < transforms.length; i++){
            if(differents.contains(transforms[i])){
                count = count;
            }
            else{
                differents.add(transforms[i]);
                count++;
            }
        }
        return count;
        
    }
}
