//Java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] returnList = new int[2];
        for (int i = 0; i < nums.length; i++){
            for (int j = 0; j < nums.length; j++){
                if (i != j){
                    if (nums[i] + nums[j] == target){
                        returnList[0] = i;
                        returnList[1] = j;
                        return returnList;
                    }
                }
            }
        }
        return returnList;
    }
}
