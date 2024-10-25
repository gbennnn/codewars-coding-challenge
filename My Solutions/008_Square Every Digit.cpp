/*
Codewars Coding Challenge

Square Every Digit
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)
Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)
Note: The function accepts an integer and returns an integer.
Happy Coding!

https://www.codewars.com/kata/546e2562b03326a88e000020/train/cpp
*/


// My Solution
#include <iostream>
#include <string>
using namespace std;
int square_digits(int num){
    string result = ""; // utk menyimpan hasil
    string konv_num = to_string(num); // konversi num to string
    // lakukan looping di setiap digit konv_num (pake foreach loop)
    for(char digit : konv_num){
        int square = (digit - '0') * (digit - '0'); // hitung kuadrat 
        result += to_string(square); // masukan hasil kuadrat ke result dan mengonversinya ke string
    }
    return stoi(result); // balikan result menjadi integer
}


// Sample test
/*
Describe(Square_Every_Digit)
{
    It(Sample_tests)
    {       
        Assert::That(square_digits(3212), Equals(9414));   
        Assert::That(square_digits(2112), Equals(4114)); 
        Assert::That(square_digits(0), Equals(0));
        Assert::That(square_digits(13579), Equals(19254981));   
        Assert::That(square_digits(24680), Equals(41636640)); 
    }  
};

*/




/*
PERFECT SOLUTION FROM CODEWARS

=1=
int square_digits(int n) {
  int a = 1;
  int m = 0;
  while (n > 0) {
    int d = n % 10;
    m += a * d * d;
    a *= d <= 3 ? 10 : 100;
    n /= 10;
  }
  return m;
}


=2=
#include <string>

int square_digits(int num) {
  
  std::string s = std::to_string(num);
  std::string ans;
  for(char c: s){
    int i = c - '0';
    ans += std::to_string(i * i);    
  }
  return std::stoi(ans);
}


=3=
int square_digits(int num) {
  
  int total = 0;
  int mul = 1;
  
  while(num) {
    int d = num % 10;
    total += d * d * mul;
    mul *= (d > 3 ? 100 : 10);
    num /= 10;
  }
  
  return total;
}


=4=
int square_digits(int num) 
{
  int square = 0;
	for (int i = 1; num != 0; i *= 10, num /= 10)
	{
		square += num % 10 * (num % 10) * i;
		if (num % 10 * (num % 10) > 10) i *= 10;
	}
	return square;
}


=5=
int square_digits(int num) {
  std::string stack = ""; 
  if (num == 0) return 0;
  while (num > 0){
    auto d = std::to_string((num % 10)*(num % 10));
    num /= 10; stack.insert(0,d); 
  }
 return std::stoi(stack);
}
*/