import java.util.ArrayList;
import java.util.Scanner;
public class main {
	public static void main(String[] args) {
		Chess newGame = new Chess();
		Scanner inp = new Scanner(System.in);
		printBoard(newGame);
		
	}
	public static void printBoard(Chess game) {
		String[][] temp = game.getBoard();
		for (int i = 0; i < temp.length; i++) {
			for (int j = 0; j < temp[i].length; j++) {
				if (j == temp[i].length-1) {
					System.out.print(temp[i][j]);
				}
				else {
				System.out.print(temp[i][j] + ", ");
				}
			}
			System.out.println();
		}
	}
}

