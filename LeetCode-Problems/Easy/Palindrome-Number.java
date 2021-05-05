//Java
class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0){
            return false;
        }
        if (x > 0 && x < 10){
            return true;
        }
        String palindrome = Integer.toString(x);
        String reverse = "";
        for (int i = palindrome.length()-1; i >= 0; i--){
            reverse += palindrome.substring(i, i+1);
        }
        if (reverse.equals(palindrome)){
            return true;
        }
        else{
            return false;
        }
    }
}
