import java.io.*;
import java.util.*;

class three {
  public static boolean find(char val, String str) {
    for(int i = 0; i < str.length(); i++) {
      if(str.charAt(i) == val) return true;
    }
    return false;
  }

  public static void problem(String input, PrintWriter out) {
    String[] strs = input.split("\\s+");
    char[] values = {
      '0','1','2','3','4','5','6','7','8','9',
      'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
      'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
    };
    for(int j = 0; j < values.length; j++) {
      boolean result = true;
      for(int i = 0; i < strs.length; i++) {
        if(!find(values[j], strs[i])) result = false;
      }
      if(result) out.print(values[j]);
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