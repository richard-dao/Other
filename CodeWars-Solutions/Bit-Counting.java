//Java
public class BitCounting {

  public static int countBits(int n){
    // Show me the code!
    String nBin = Integer.toBinaryString(n);
    int count = 0;
    for (int i = 0; i < nBin.length(); i++){
      if (nBin.charAt(i) == '1'){
        count++;
      }
    }
    return count;
  }
  
}
