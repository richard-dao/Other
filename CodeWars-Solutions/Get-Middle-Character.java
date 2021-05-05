//Java
class Kata {
  public static String getMiddle(String word) {
    //Code goes here!
    if (word.length() % 2 == 0){
      return word.substring((word.length()/2)-1, (word.length()/2)+1);
    }
    else{
      return word.substring(word.length()/2, (word.length()/2)+1);
    }
  }
}
