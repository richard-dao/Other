
public class Chess {
	private static String[][] chBoard;
	private static String[][] backEndBoard;
	private boolean gameOver = false;
	private static int totalMoves = 0;
	
	public Chess() {
		// Initialize an 8x8 matrix/2d array for the board
		chBoard = new String[8][8];  
		backEndBoard = new String[8][8];
		
		// Set each place with a coordinate (a1-h8)
		for (int i = 0; i < chBoard.length; i++) {
			for (int j = chBoard[i].length-1; j >= 0; j--) {
				int ascii = i + 97;
				String letter = Character.toString((char) ascii);
				chBoard[j][i] = letter + Integer.toString(8-j);
			}
		}
		
		//
		for (int i = 0; i < backEndBoard.length; i++) {
			for (int j = backEndBoard[i].length-1; j >= 0; j--) {
				int ascii = i + 97;
				String letter = Character.toString((char) ascii);
				chBoard[j][i] = letter + Integer.toString(8-j);
			}
		}
		
		// Set each piece to default square
		initiatePieces();
		
	}
	
	public String[][] getBoard(){
		return chBoard;
	}
	public boolean getStatus() {
		return gameOver;
	}
	
	public static void initiatePieces() {
		
		
	}
	
	public static void movePiece(String move) {
		String copyMove = move;
		int moveLeng = copyMove.length();
		totalMoves++;
		if (totalMoves % 2 == 0) { // Black's Move
			if (moveLeng == 6) {
				
			}
			else if (moveLeng == 5) {
				
			}
			else if (moveLeng == 4) {
				
			}
			else if (moveLeng == 3) {
				
			}
			else if (moveLeng == 2) {
				
			}
			else {
				return;
			}
		}
		else { // White's move
			if (moveLeng == 6) {
				
			}
			else if (moveLeng == 5) {
				
			}
			else if (moveLeng == 4) {
				
			}
			else if (moveLeng == 3) {
				
			}
			else if (moveLeng == 2) {
				
			}
			else {
				return;
			}
		}	
	}
}

