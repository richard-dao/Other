//Java
class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        ArrayList<Boolean> returnedList = new ArrayList<Boolean>(candies.length);
        int max = 0;
        for (int i = 0; i < candies.length; i++){
            if (candies[i] > max){
                max = candies[i];
            }
        }
        for (int i = 0; i < candies.length; i++){
            if (candies[i] + extraCandies >= max){
                returnedList.add(true);
            }
            else{
                returnedList.add(false);
            }
        }
        return returnedList;
    }
}
