import java.io.*;
import java.util.*;

class four {

  public static double trade(String input, double cash) {
    double endCash = cash;
    String[] strArr = input.split("\\s+");
    double[] prices = new double[strArr.length];
    for(int i = 1; i < strArr.length; i++) prices[i] = Double.parseDouble(strArr[i]);
    String ticker = strArr[0];
    boolean holding = false;
    for(int i = 1; i < prices.length - 1; i++) {
      if(i > 1 && holding) endCash += prices[i] - prices[i - 1];
      if(!holding && prices[i + 1] > prices[i]) holding = true;
    }
    return endCash;
  }

  public static void tradePrint(String input, double cash, String hours, PrintWriter out) {
    double endCash = cash;
    String[] strArr = input.split("\\s+");
    double[] prices = new double[strArr.length];
    for(int i = 1; i < strArr.length; i++) prices[i] = Double.parseDouble(strArr[i]);
    String ticker = strArr[0];
    out.println(ticker);
    out.println(hours);
    boolean holding = false;
    for(int i = 1; i < prices.length - 1; i++) {
      if(i > 1 && holding) {
        endCash += prices[i] - prices[i - 1];
        out.print(".   ");
      }
      if(!holding && prices[i + 1] > prices[i]) {
        holding = true;
        out.print("B   ");
      }
      if(holding && prices[i] > prices[i + 1]) {
        holding = false;
        out.print("S   ");
      }
    }
    out.println();
    out.println(endCash);
  }

  public static void main(String[] args) throws IOException {
    Scanner in = new Scanner(new File(args[0]));
    PrintWriter out = new PrintWriter(new File("output.txt"));
    double cash = Double.parseDouble(in.nextLine());
    double maxGains = 0;
    String hours = in.nextLine();
    String[] stocks;
    // while(in.hasNextLine()) stocks[stocks.length - 1] = in.nextLine();
    // for(int i = 0; i < stocks.length; i++) out.println(trade(stocks[i], cash));
    in.nextLine();
    in.nextLine();
    tradePrint(in.nextLine(), cash, hours, out);

    in.close();
    out.close();
  }
}