//Java
class Solution {
    public int[] decompressRLElist(int[] nums) {
        int[] currentPair = new int[2];
        ArrayList<Integer> returnedList = new ArrayList<Integer>();
        for (int i = 0; i < nums.length; i+=2){
            currentPair[0] = nums[i];
            currentPair[1] = nums[i+1];
            for (int j = 0; j < currentPair[0]; j++){
                returnedList.add(currentPair[1]); 
            }
        }
        int[] returnedIntList = new int[returnedList.size()];
        for (int i = 0; i < returnedList.size(); i++){
            returnedIntList[i] = returnedList.get(i);
        }
        return returnedIntList;
    }
}
