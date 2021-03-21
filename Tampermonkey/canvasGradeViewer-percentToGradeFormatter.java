import java.util.*;
import java.text.*;
import java.io.*;

public class main {
	public static void main(String[] args) {
		ArrayList<Double> s = new ArrayList<Double>();
		ArrayList<String> sd = new ArrayList<String>();
		double percentages = 0.00;
		for (int i = 0; i < 10000; i++) {
			DecimalFormat df = new DecimalFormat("#.##");
			double p = Double.parseDouble(df.format(percentages+0.01));
			s.add(p);
			percentages = percentages + 0.01;

		}
		
		for (int i = s.size()-1; i >= 0; i--) {
			String value = "\"F\" ";
			String text = Double.toString(Math.abs(s.get(i)));
			
			if (s.get(i) < 60.00) {
				value = "\"F\" ";
				sd.add("[/" + Double.toString(s.get(i)) + "%/i, " + value + "],");
			}
			else if (s.get(i) < 70.00) {
				if (s.get(i) < 63.00) {
					value = "\"D-\"";
					sd.add("[/" + Double.toString(s.get(i)) + "%/i, " + value + "],");
				}
				else if (s.get(i) < 67.00) {
					value = "\"D\"";
					sd.add("[/" + Double.toString(s.get(i)) + "%/i, " + value + "],");
				}
				else {
					value = "\"D+\"";
					sd.add("[/" + Double.toString(s.get(i)) + "%/i, " + value + "],");
				}
			}
			else if (s.get(i) < 80.00) {
				if (s.get(i) < 73.00) {
					value = "\"C-\"";
					sd.add("[/" + Double.toString(s.get(i)) + "%/i, " + value + "],");
				}
				else if (s.get(i) < 77.00) {
					value = "\"C\"";
					sd.add("[/" + Double.toString(s.get(i)) + "%/i, " + value + "],");
				}
				else {
					value = "\"C+\"";
					sd.add("[/" + Double.toString(s.get(i)) + "%/i, " + value + "],");
				}
			}
			else if (s.get(i) < 90.00) {
				if (s.get(i) < 83.00) {
					value = "\"B-\"";
					sd.add("[/" + Double.toString(s.get(i)) + "%/i, " + value + "],");
				}
				else if (s.get(i) < 87.00) {
					value = "\"B\"";
					sd.add("[/" + Double.toString(s.get(i)) + "%/i, " + value + "],");
				}
				else {
					value = "\"B+\"";
					sd.add("[/" + Double.toString(s.get(i)) + "%/i, " + value + "],");
				}
			}
			else if (s.get(i) <= 100.00) {
				if (s.get(i) < 93.00) {
					value = "\"A-\"";
					sd.add("[/" + Double.toString(s.get(i)) + "%/i, " + value + "],");
				}
				else if (s.get(i) < 97.00) {
					value = "\"A\"";
					sd.add("[/" + Double.toString(s.get(i)) + "%/i, " + value + "],");
				}
				else {
					value = "\"A+\"";
					sd.add("[/" + Double.toString(s.get(i)) + "%/i, " + value + "],");
				}
			}
		}
		String c = "";
		for (int i = 0; i < sd.size(); i++) {
			c += sd.get(i);
		}
		System.out.println(c.length());
		
		try {
		      File myObj = new File("percentToLetter.txt");
		      if (myObj.createNewFile()) {
		        System.out.println("File created: " + myObj.getName());
		      } else {
		        System.out.println("File already exists.");
		      }
		    } catch (IOException e) {
		      System.out.println("An error occurred.");
		      e.printStackTrace();
		    }
		try {
		      FileWriter myWriter = new FileWriter("percentToLetter.txt");
		      myWriter.write(c);
		      myWriter.close();
		      System.out.println("Successfully wrote to the file.");
		    } catch (IOException e) {
		      System.out.println("An error occurred.");
		      e.printStackTrace();
		    }
  }
  
}
