//Java
class Solution {
    public int diagonalSum(int[][] mat) {
        int sum = 0;
        
        int j = mat.length-1;
        for (int i = 0; i < mat.length; i++){
            int addLR = mat[i][i];
            int addRL = mat[i][j];
            sum = sum + addLR + addRL;
            j--;
        }
        if (mat.length % 2 == 1){
            int middle = mat[mat.length/2][mat.length/2];
            sum = sum - middle;
        }
        return sum;
    }
}
