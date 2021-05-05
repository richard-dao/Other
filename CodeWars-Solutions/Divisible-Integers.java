//Java
import java.util.ArrayList;
public class Kata
{
  public static int getCount(int n)
  {
    // your code
    int count = 0;
    String strN = Integer.toString(n);
    ArrayList<String> sNList = new ArrayList<String>();
    int[] sConvert;
    
    for (int i = 0; i < strN.length()+1; i++){
      for (int j = i; j < strN.length()+1; j++){
        sNList.add(strN.substring(i, j));
      }
    }
    for (int i = 0; i < sNList.size(); i++){
      if (sNList.get(i).equals("")){
        sNList.remove(i);
        i--;
      }
      else if (sNList.get(i).equals("0")){
        sNList.remove(i);
        i--;
      }
      else if (sNList.get(i).equals(strN)){
        sNList.remove(i);
        i--;
      }
    }
    sConvert = new int[sNList.size()];
    for (int i = 0; i < sNList.size(); i++){
      sConvert[i] = Integer.parseInt(sNList.get(i));
    }
    
    for (int i = 0; i < sConvert.length; i++){
      if (sConvert[i] != 0){
        if (n % sConvert[i] == 0){
          count++;
        }
      }
    }
    return count;
  }
}
