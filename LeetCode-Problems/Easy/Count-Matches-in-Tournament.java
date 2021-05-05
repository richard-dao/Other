//Java
class Solution {
    public int numberOfMatches(int n) {
        int count = 0;
        int teamsLeft = n;
        
        while (teamsLeft > 1){
            if (teamsLeft % 2 == 0){
                count += teamsLeft/2;
                teamsLeft = teamsLeft/2;
            }
            if (teamsLeft % 2 == 1){
                count += teamsLeft/2;
                teamsLeft++;
                teamsLeft = teamsLeft/2;
            }
        }
        return count;
    }
}
