/*
Codewars Coding Challenge

Sum of Digits / Digital Root
Digital root is the recursive sum of all the digits in a number.
Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.

Examples
16  -->  1 + 6 = 7
942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11

https://www.codewars.com/kata/541c8630095125aba6000c00/train/cpp
*/


// My Solution
// #include <iostream>
// using namespace std;

int digital_root(int n)
{
    int sum = 0;

    // Menangani kasus bilangan negatif
    if (n < 0) {
        // Mengembalikan -1 untuk menandakan kesalahan
        return -1;
    }

    // Menghitung jumlah digit bilangan sampai hanya satu digit tersisa
    while (n > 0 || sum > 9) {
        if (n == 0) {
            n = sum;
            sum = 0;
        }
        sum += n % 10;
        n /= 10;
    }

    // Mengembalikan hasil digital root
    return sum;
}

// int digital_root(int n){
//     int sum = 0;
//     while(n > 0 || sum > 9){
//         if(n == 0){
//             n = sum;
//             sum = 0;
//         }
//         sum += n % 10;
//         n /= 10;
//     }

//     return sum;
// }

// int main(){
//     // system("cls")

//     int n;
//     do{
//         cout << "Masukkan angka: ";
//         cin >> n;
//         cout << "Hasil = " << digital_root(n) << endl;
//     }while(true);



//     return 0;
// }

// Sample test
/*Describe(Fixed_tests)
{
    It(Digital_root)
    {
        Assert::That(digital_root(16) , Equals(7));
        Assert::That(digital_root(195) , Equals(6));
        Assert::That(digital_root(992) , Equals(2));
        Assert::That(digital_root(167346) , Equals(9));
        Assert::That(digital_root(0) , Equals(0));
    }
};
*/


// Other solution

// PERFECT SOLUTION

// =1=
// int digital_root(int Z) {
//     return --Z % 9 + 1;
// }

// =2=
// int digital_root(int n)
// {
//   return (n-1) % 9 +1;
// }

// =3=
// int digital_root(int n)
// {
//   if(n < 10) 
//     return n;
//   return digital_root(n % 10 + digital_root(n / 10));
// }

// =4=
// int digital_root(int n)
// {
// /*
// a number of can be represented in the form of 9k+i where 0<=i<=8
// a remainder of i means digital root i if it's a natural number
// for 0 its 0
//  */
// if(not n)return n;
//   n%=9;
//     return n?n:9;
// }

// =5=
// int digital_root(int n)
// {
//   int sum = 0;
  
//   while(n > 0)
//   {
//     sum += (n % 10);
//     n = (n / 10);
//   }
  
//   return sum < 10 ? sum : digital_root(sum);
// }