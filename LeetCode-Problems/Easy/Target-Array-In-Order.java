//Java
class Solution {
    public int[] createTargetArray(int[] nums, int[] index) {
        ArrayList<Integer> arrList = new ArrayList<Integer>(index.length);
        for (int i = 0; i < index.length; i++){
            arrList.add(index[i], nums[i]);
        }
        int[] returnList = new int[arrList.size()];
        for (int i = 0; i < arrList.size(); i++){
            returnList[i] = arrList.get(i);
        }
        return returnList;
    }
}
