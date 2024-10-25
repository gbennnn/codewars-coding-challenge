/* Codewars Coding Challenge

    Day 80/366

    Level 7kyu

Snail crawls up

The snail crawls up the column. During the day it crawls up some distance. During the night she sleeps, so she slides down for some distance (less than crawls up during the day).

Your function takes three arguments:

The height of the column (meters)
The distance that the snail crawls during the day (meters)
The distance that the snail slides down during the night (meters)
Calculate number of day when the snail will reach the top of the column.


public class Kata {
    public static int snail(int column, int day, int night) {
      return 0; // your code here
    }
}

https://www.codewars.com/kata/5b93fecd8463745630001d05/train/java

 */
public class Kata {
    public static int snail(int column, int day, int night) {
        int height = 0;
        int days = 0;

        while (height < column) {
            height += day;
            if (height >= column) {
                days++;
                break;
            }
            height -= night;
            days++;
        }
        return days;
    }

    // Test Cases
    public static void main(String[] args) {
        System.out.println(snail(3, 2, 1));
        System.out.println(snail(10, 3, 1));
        System.out.println(snail(10, 3, 2));
        System.out.println(snail(100, 20, 5));
        System.out.println(snail(5, 10, 3));
    }
}


/*
Sample Tests

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import org.junit.runners.JUnit4;

public class SampleTest {
    @Test
    public void basicTests() {
        assertEquals(2, Kata.snail(3,2,1));
        assertEquals(5, Kata.snail(10,3,1));
        assertEquals(8, Kata.snail(10,3,2));
        assertEquals(7, Kata.snail(100,20,5));
        assertEquals(1, Kata.snail(5,10,3));
    }
}
 */
