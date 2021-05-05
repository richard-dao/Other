//Java
public class Sum{
  public static void main(String[] args){
    int a = 0;
    int b = 1;
    int sum = 0;
    if (a == b){
      return a;
    }
    if (a < b){
      sum = a;
      for (int i = a; i < b; i++){
        sum += i + 1;
      }
      return sum;
    }
    if (a > b){
      sum = b;
      for (int i = b; i < a; i++){
        sum += i + 1;
      }
      return sum;
    } 
    return sum;
  }
}
