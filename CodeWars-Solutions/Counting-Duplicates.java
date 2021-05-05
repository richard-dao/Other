//Java
import java.util.ArrayList;
public class CountingDuplicates {
  public static int duplicateCount(String text) {
    // Write your code here
    int sum = 0;
    String temp = text.toLowerCase();
    ArrayList<String> foundLetters = new ArrayList<String>();
    int count = 0;
    for (int i = 0; i < temp.length(); i++){
      count = 0;
      for (int j = i+1; j < temp.length(); j++){
        if (temp.substring(i, i+1).equals(temp.substring(j, j+1))){
          if (!(foundLetters.contains(temp.substring(i, i+1)))){
            count++;
            foundLetters.add(temp.substring(i, i+1));
          }
        }  
      }
      if (count > 0){
        sum++;
      } 
    }
    return sum;
  }
}
