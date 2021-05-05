//Java
class Solution {
    public int searchInsert(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++){
            if (target == nums[i]){
                return i;
            }
        }
        int x = 0;
        while (x < nums.length){
            if (nums[x] < target){
                x++;
            }
            else{
                return x;
            }
        }
        return x;
    }
}
