/*
Codewars Coding Challenge

Build Tower
Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.
For example, a tower with 3 floors looks like this:

[
  "  *  ",
  " *** ", 
  "*****"
]
And a tower with 6 floors looks like this:

[
  "     *     ", 
  "    ***    ", 
  "   *****   ", 
  "  *******  ", 
  " ********* ", 
  "***********"
]
Go challenge Build Tower Advanced once you have finished this :)

https://www.codewars.com/kata/576757b1df89ecf5bd00073b/train/cpp
*/



// My Solution
#include <string>
#include <vector>

std::vector<std::string> towerBuilder(unsigned nFloors) {
    std::vector<std::string> tower;
    int maxStars = nFloors * 2 - 1; // Jumlah maksimum bintang pada lantai terakhir

    for (unsigned i = 0; i < nFloors; ++i) {
        int numStars = 2 * i + 1; // Jumlah bintang pada lantai ini
        int numSpaces = (maxStars - numStars) / 2; // Jumlah spasi di awal dan akhir

        std::string floor = std::string(numSpaces, ' ') + std::string(numStars, '*') + std::string(numSpaces, ' ');
        tower.push_back(floor); // Tambahkan lantai ke dalam vector
    }

    return tower;
}

/*
#include <iostream>
using namespace std;

int main(){
  for(int i = 1; i <= 6; i++){
    for(int j = 1; j <= 6-i; j++){
      cout << " ";
    }
    for(int k = 1; k <= i; k++){
        cout << " * ";
    }
    cout << endl;
  }
  
  return 0;
}
*/



// Sample test
/*
#include <string>
#include <vector>

Describe(Tests)
{
    It(ExampleTest1)
    {
        std::vector<std::string> expected = { "*" };
 
        std::vector<std::string> actual = towerBuilder(1);
    
        Assert::That(actual, Is().EqualTo(expected));
    }
    
    It(ExampleTest2)
    {
        std::vector<std::string> expected = { " * ", "***" };
        
        std::vector<std::string> actual = towerBuilder(2);
    
        Assert::That(actual, Is().EqualTo(expected));
    }
    
    It(ExampleTest3)
    {
        std::vector<std::string> expected = { "  *  ", " *** ", "*****" };
        
        std::vector<std::string> actual = towerBuilder(3);
    
        Assert::That(actual, Is().EqualTo(expected));
    }
};
*/




/*
PERFECT SOLUTION FROM CODEWARS

=1=
#include <string>
#include <vector>

using namespace std;

vector<string> towerBuilder(unsigned nFloors) {
  vector <string> vect;
  for(unsigned i = 0, k = 1; i < nFloors; i++, k+=2)
    vect.push_back(string(nFloors-i-1, ' ') + string(k, '*') + string(nFloors-i-1, ' '));
  return {vect};
}


=2=
#include <string>
#include <vector>

std::vector<std::string> towerBuilder(unsigned nFloors) {
  std::vector<std::string> tower;
  for(unsigned i = 1; i <= nFloors; i++){
     std::string floor = std::string(nFloors - i, ' ') + std::string(i*2 - 1, '*') + std::string(nFloors - i, ' ');
     tower.push_back(floor);
   }
   return tower;    
};


=3=
#include <string>
#include <vector>

std::vector<std::string> towerBuilder(unsigned n) {
  std::vector<std::string> tower = {};
  for(int i = 1; i <= n; i++){
      std::string stars(2 * i - 1, '*');
      std::string spaces(n - i, ' ');
      tower.push_back(spaces + stars + spaces);
  }
  return tower;
}


=4=
#include <string>
#include <vector>

std::vector<std::string> towerBuilder(unsigned nFloors) {
  std::vector<std::string> tower;
  for (size_t i = 1; i <= nFloors; i++) {
    std::string stars(i * 2 - 1, '*');
    std::string spaces(nFloors - i, ' ');
    std::string floor = spaces + stars + spaces;
    tower.push_back(floor);
  }
  return tower;
}


=5=
#include <string>
#include <vector>
using namespace std;

std::vector<std::string> towerBuilder(unsigned nFloors) {
  std::vector<std::string> result(nFloors, std::string(nFloors*2-1, ' '));
  for (unsigned int i=0;i<nFloors;i++)
    result[i].replace((nFloors*2-1)/2-i,i*2+1,std::string(i*2+1, '*'));
  return result;
}
*/