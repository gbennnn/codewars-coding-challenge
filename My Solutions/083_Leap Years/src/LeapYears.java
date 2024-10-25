/*
Codewars Coding Challenge

Day 83/366

Level 7kyu

Leap Years

In this kata you should simply determine, whether a given year is a leap year or not. In case you don't know the rules, here they are:

Years divisible by 4 are leap years,
but years divisible by 100 are not leap years,
but years divisible by 400 are leap years.
Tested years are in range 1600 ≤ year ≤ 4000.


public class LeapYears {

  public static boolean isLeapYear(int year) {
    return true;
  }
}


https://www.codewars.com/kata/526c7363236867513f0005ca/train/java

 */
public class LeapYears {

    public static boolean isLeapYear(int year) {
      if(year % 4 == 0){
        if(year % 100 == 0){
          return year % 400 == 0;
        } else{
          return true;
        }
      } else{
        return false;
      }
    }
  }
