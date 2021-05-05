//Java
class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int[] rArr = new int[2];
        for (int i = 0; i < numbers.length; i++){
            for (int j = i+1; j < numbers.length; j++){
                if (numbers[i] + numbers[j] == target){
                    rArr[0] = i+1;
                    rArr[1] = j+1;
                    return rArr;
                }
            }
        }
        return rArr;
    }
}
