import java.io.*;
import java.util.*;

class one {
  public static boolean find(String val, String str) {
    for(int i = 0; i < strs.length; i++) {
      if(ints[i] == val) return true;
    }
    return false;
  }

  public static void problem(String input, PrintWriter out) {
    String[] strs = input.split("\\s+");
    String[] values = {
      "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
    }
    for(int j = 0; j < values.length; j++) {
      boolean result = true;
      for(int i = 0; i < strs.length; i++) {
        if(!find(values[j], strs[i])) result = false;
      }
    }
  }

  public static void main(String[] args) throws IOException {
    Scanner in = new Scanner(new File(args[0]));
    PrintWriter out = new PrintWriter(new File("output.txt"));
    int n = Integer.parseInt(in.nextLine());
    for(int i = 0; i < n; i++) {
      problem(in.nextLine(), out);
      out.println();
    }

    in.close();
    out.close();
  }
}