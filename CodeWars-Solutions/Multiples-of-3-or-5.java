//Java
public class Solution {
  public int solution(int number) {
    //TODO: Code stuff here
    int sum = 0;
    int tempNum = number-1;
    while(tempNum >= 0){
      if (tempNum % 5 == 0 || tempNum % 3 == 0){
        sum += tempNum;
        tempNum--;
      }
      else{
        tempNum--;
      }
    }
    return sum;
  }
}
