//Java
class Solution {
    public int findNumbers(int[] nums) {
        int count = 0;
        for (int i = 0; i < nums.length; i++){
            int numLength = Integer.toString(nums[i]).length();
            if (numLength % 2 == 0){
                count++;
            }
        }
        return count;
    }
}
