//Java
class Solution {
    public int maximumWealth(int[][] accounts) {
        int solution = 0;
        for (int i = 0; i < accounts.length; i++){
            int currentEvaluation = 0;
            for (int j = 0; j < accounts[i].length; j++){
                currentEvaluation += accounts[i][j];
            }
            solution = Math.max(solution, currentEvaluation);
        }
        return solution;
    }
}
