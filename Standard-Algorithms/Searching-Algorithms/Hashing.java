//Java 
//Many different hashing algorithms; I use the popularly used djb2 algorithm
//djb2 Hashing Algorithm
public int hash(String str) {
		int hash = 0;
		int leftShiftValue = 1;
		
		for (int i = 0; i < 2; i++) {
			if (str.length() > i) {
				hash = str.charAt(i) + ((hash << leftShiftValue) - hash);
			}
		}
		return hash;
	}

String[] stringArr = new String[253];

//Insertion and Search using Hashing
stringArr[hash("One")] = "1";
stringArr[hash("Two")] = "2";
stringArr[hash("Three")] = "3";

System.out.println(stringArr[hash("Three")]);
