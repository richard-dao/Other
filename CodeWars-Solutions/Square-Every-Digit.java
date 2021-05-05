//Java
public class SquareDigit {

  public int squareDigits(int n) {
    // TODO Implement me
    int y = n;
    int length = String.valueOf(n).length();
    int[] squareDigits = new int[length];
    String[] stringSquares = new String[length];
    for (int i = squareDigits.length-1; i >= 0; i--){
      squareDigits[i] = (y % 10) * (y % 10);
      y = y/10;
    }
    for (int i = 0; i < length; i++){
      stringSquares[i] = Integer.toString(squareDigits[i]);
    }
    String returnedString = "";
    for (int i = 0; i < length; i++){
      returnedString += stringSquares[i];
    }
    return Integer.parseInt(returnedString);
  }

}
