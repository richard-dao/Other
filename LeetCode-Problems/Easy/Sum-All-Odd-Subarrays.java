//Java
class Solution {
    public int sumOddLengthSubarrays(int[] arr) {
        int sum = 0;
        if (arr.length == 0 || Objects.isNull(arr.length)){
            return 0;
        }
        for (int i = 0; i < arr.length; i++){
            int temp = 0;
            for (int j = i; j < arr.length; j++){
                temp += arr[j];
                if ((j-i) % 2 == 0){
                    sum += temp;
                }
            }
        }
        return sum;
    }
}
