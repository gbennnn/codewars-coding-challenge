/* Codewars Coding Challenge

Day 82/366

Level 7kyu

Running out of space

Kevin is noticing his space run out! Write a function that removes the spaces from the values and returns an array showing the space decreasing.
For example, running this function on the array ['i', 'have','no','space'] would produce ['i','ihave','ihaveno','ihavenospace']


public class OutOfSpace {
  
  public static String[] spacey(String[] array) {
    // TODO: Figure it out :)
    return null;
  }
  
}


https://www.codewars.com/kata/56576f82ab83ee8268000059/train/java
 * 
 * 
 */

public class OutOfSpace {
    public static String[] spacey(String[] array) {
      String[] result = new String[array.length];
      String noSpace = "";
      for (int i = 0; i < array.length; i++) {
          noSpace += array[i];
          result[i] = noSpace;
      }
      return result;
    }
  }
  

  /*
   * Sample Tests
   * 
   * 
   * import java.util.Arrays;
import org.junit.jupiter.api.*;

@TestMethodOrder(MethodOrderer.OrderAnnotation.class)
class SolutionTest {

    @Test
    @Order(1)
    @DisplayName("Strings with lower letters only")
    void test1() {
        String[] input = new String[]{"kevin", "has", "no", "space"};
        String[] expected = new String[]{"kevin", "kevinhas", "kevinhasno", "kevinhasnospace"};
        Assertions.assertArrayEquals(expected, OutOfSpace.spacey(input));
    }

    @Test
    @Order(2)
    @DisplayName("Strings with camel case")
    void test2() {
        String[] input = new String[]{"Camel", "Case", "Should", "Remain"};
        String[] expected = new String[]{"Camel", "CamelCase", "CamelCaseShould", "CamelCaseShouldRemain"};
        Assertions.assertArrayEquals(expected, OutOfSpace.spacey(input));
    }

    @Test
    @Order(3)
    @DisplayName("Strings with letters, digits,")
    void test3() {
        String[] input = new String[]{"Trying!", "Adding2", "Diff3rent", "Comb1nati0ns"};
        String[] expected = new String[]{"Trying!", "Trying!Adding2", "Trying!Adding2Diff3rent", "Trying!Adding2Diff3rentComb1nati0ns"};
        Assertions.assertArrayEquals(expected, OutOfSpace.spacey(input));
    }


}

   */