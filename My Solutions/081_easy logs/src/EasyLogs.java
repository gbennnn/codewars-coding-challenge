/*
Codewars Coding Challenge 

Day 81/366

Level 8kyu

Easy Logs

problem : \My Solutions\081_easy logs\problem\image.png

https://www.codewars.com/kata/5b68c7029756802aa2000176/train/java

 */

public class EasyLogs {
    public static double logs(double x, double a, double b) {
      double resultA = Math.log(a) / Math.log(x);
      double resultB = Math.log(b) / Math.log1p(x);
      double sum = resultA + resultB;
      return sum;
    }

    public static void main(String[] args) {
      double base = 10; // Base of the logarithms
      double A = 5;     // Value A
      double B = 2;     // Value B

      double sum = logs(base, A, B);

      // Print the result
      System.out.println("Sum of logarithms: " + sum);
  }
  
  }