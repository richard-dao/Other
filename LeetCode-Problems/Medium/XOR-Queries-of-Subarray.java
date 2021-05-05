//Java
class Solution {
    public int[] xorQueries(int[] arr, int[][] queries) {
        int[] rArr = new int[queries.length];
        int sum = 0;
        for (int i = 0; i < queries.length; i++){
            int start = queries[i][0];
            int end = queries[i][1];
            sum = arr[start];
            for (int j = start; j < end; j++){
                sum = (sum ^ arr[j+1]);
            }
            rArr[i] = sum;
        }
        return rArr;   
    }
}
