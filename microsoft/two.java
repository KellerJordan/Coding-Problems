import java.io.*;
import java.util.*;

class two {

  public static void problem(String str, PrintWriter out) {
    String[] colors = str.split("\\s+");
    String prev = "";
    for(int i = 0; i < colors.length - 1; i++) {
      String color = colors[i];
      String result = "";
      if(i == 0) {
        result = color;
      } else {
        if(color.equals("green")) {
          if(prev.equals("yellow")) result = "blue";
          else result = "yellow";
        } else if(color.equals("orange")) {
          if(prev.equals("red")) result = "yellow";
          else result = "red";
        } else if(color.equals("purple")) {
          if(prev.equals("red")) result = "blue";
          else result = "red";
        } else {
          if(prev.equals("blank")) result = color;
          else result = "blank";
        }
      }
      prev = result;
      out.print(result);
      if(i < colors.length - 2) out.print(" ");
    }
  }

  public static void main(String[] args) throws IOException {
    Scanner in = new Scanner(new File(args[0]));
    PrintWriter out = new PrintWriter(new File("output.txt"));
    problem(in.nextLine(), out);

    in.close();
    out.close();
  }
}