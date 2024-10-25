/*
Codewars coding challenge

A square of squares
You like building blocks. You especially like building blocks that are squares. And what you even like more, is to arrange them into a square of square building blocks!
However, sometimes, you can't arrange them into a square. Instead, you end up with an ordinary rectangle! Those blasted things! If you just had a way to know, whether you're currently working in vain… Wait! That's it! You just have to check if your number of building blocks is a perfect square.

Task
Given an integral number, determine if it's a square number:
In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself.

The tests will always use some integral number, so don't worry about that in dynamic typed languages.

Examples
-1  =>  false
0  =>  true
3  =>  false
4  =>  true
25  =>  true
26  =>  false

https://www.codewars.com/kata/54c27a33fb7da0db0100040e/train/cpp
*/

// My Solution
bool is_square(int n) {
    // n kurang dari nol bukan kuadrat sempurna
    if(n < 0){
        return false;
    }

    // 0 dan 1 adalah kuadrat sempurna
    if(n == 0 || n == 1){
        return true;
    }

    // Deklarasi variabel
    int i = 0; //untuk iterasi berawal dari 0
    int result = 0; //result diberi nilai awal 0

    // lakukan iterasi
    while(i < n){
        result = i * i; // setiap iterasi akan dikuadratkan dan hasilnya disimpan ke dalam variabel result

        // Jika result sama dengan n maka n merupakan kuadrat sempurna
        if(result == n){
            return true;
        }
        i++;
    }

    // Selain dari itu semua adalah salah
    return false;
}

// Sample test
// Describe(is_square_function)
// {
//     It(should_work_for_basic_tests)
//     {
//         Assert::That(is_square(-1), Equals(false));
//         Assert::That(is_square(0), Equals(true));
//         Assert::That(is_square(3), Equals(false));
//         Assert::That(is_square(4), Equals(true));
//         Assert::That(is_square(25), Equals(true));
//         Assert::That(is_square(26), Equals(false));
//     }
// };

// #include <iostream>
// using namespace std;

// int main(){
//     system("cls");
//     int input;
//     while (true){
//         cout << "Masukkan angka: ";
//         cin >> input;
//         cout << is_square(input);
//     }
    

//     return 0;
// }

/*
Other solution:

=1=
bool is_square(int n)
{
  for (int i = 0; i <= n/2 + 1; i++){
  if ( i * i == n)
  return true;
  }
  return false;
}

=2=
bool is_square(int n)
{
  int temp = 1;
  while (n >= temp) {
    n -= temp;
    temp += 2;
  }
  
  return n == 0;
}

=3=
#include <cmath>

bool is_square(int n)
{
  double a = sqrt(n);
  
  if (a != (int)a){
    return false;
  }
  return true;
 
}

=4=
#include <math.h>
bool is_square(int n)
{
  return sqrt(n)==int(sqrt(n));
}

=5=
bool is_square(int n)
{
	bool squ = false;
	// TODO
	for (int i = 0; i <= n; i++) {
		if (i * i == n) {
			squ = true;
		}
	}
	return squ;
}


=6=
bool is_square(int n)
{
  if(n==0){
return 1;
  }
  for (int a=1;a<=n;a++)
  {
if(n%a==0&&n/a==a){
return 1;
  }
    }
    return 0;
  }

*/