//Java
class Solution {
    public int reverse(int x) {
        long returnedInt = 0;
        while (x != 0){
            returnedInt = returnedInt * 10;
            returnedInt = returnedInt + x % 10;
            x = x/10;
            
        }
        if (returnedInt < Integer.MIN_VALUE || returnedInt > Integer.MAX_VALUE){
            return 0;
        }
        else{
            return (int)returnedInt;
        }
    }
}
