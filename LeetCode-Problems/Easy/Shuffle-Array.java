//Java
class Solution {
    public int[] shuffle(int[] nums, int n) {
        int[] firstHalf = new int[n];
        int[] secondHalf = new int[n];
        int[] returnedArray = new int[nums.length];
        for (int i = 0; i < n; i++){
            firstHalf[i] = nums[i];
        }
        int x = 0;
        for (int i = n; i < nums.length; i++){
            secondHalf[x] = nums[i];
            x++;
        }
        int j = 0;
        for (int i = 0; i < nums.length; i+=2){
            returnedArray[i] = firstHalf[j];
            returnedArray[i+1] = secondHalf[j];
            j++;
        }
        return returnedArray;
        
    }
}
