//Java
import java.lang.StringBuilder;
class Solution {
    public String convertToTitle(int n) {
        char ascii;
        StringBuilder rStr = new StringBuilder();
        int x = n;
        while (x > 0){
            ascii = (char) (((x-1) % 26) + 65);
            rStr.insert(0, ascii);
            x = (x-1) / 26;
        }
        return rStr.toString();
    }
}
