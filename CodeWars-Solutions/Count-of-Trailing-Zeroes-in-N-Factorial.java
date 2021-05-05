//Java
public class Solution {
  public static int zeros(int n) {
    // your beatiful code here
    System.out.println(n);
    if (n == 0){
      return 0;
    }
    int sum = 0;
    for (int i = 5; n/i >= 1; i*=5){
      sum += n/i;
    }
    return sum;
  }
}
