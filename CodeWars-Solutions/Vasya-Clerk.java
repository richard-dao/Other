//Java
public class Line {
  public static String Tickets(int[] peopleInLine)
  {
        //Your code is here...
    int amount25 = 0;
    int amount50 = 0;
    int amount100 = 0;
    int change;
    for (int i = 0; i < peopleInLine.length; i++){
      change = (peopleInLine[i] - 25);
      if (peopleInLine[i] == 25){
        amount25++;
      }
      if (peopleInLine[i] == 50){
        amount50++;
      }
      if (peopleInLine[i] == 100){
        amount100++;
      }
      if (change == 25){
        if (amount25 > 0){
          amount25--;
        }
        else{
          return "NO";
        }
      }
      if (change == 75){
        if(amount25 > 0 && amount50 > 0){
          amount25--;
          amount50--;
        }
        else if(amount25 > 2){
          amount25 = amount25-3;
        }
        else{
          return "NO";
        }
      }  
    }
    return "YES";
  }
}
