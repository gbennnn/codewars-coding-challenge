/*
Codewars Coding Challenge

Replace With Alphabet Position.

In this kata you are required to, given a string, replace every letter with its position in the alphabet.
If anything in the text isn't a letter, ignore it and don't return it.
"a" = 1, "b" = 2, etc.

Example
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )

https://www.codewars.com/kata/546f922b54af40e1e90001da/train/cpp
*/


// My Solution
#include <string>

std::string alphabet_position(const std::string &text){
    std::string temp = ""; // buat variabel temp untuk menyimpan posisi alphabet
    for(char c : text){ // lakukan iterasi ke setiap karakter pada text
        if(isalpha(c)){ // periksa apakah menemukan karakter alphabet?
            temp += std::to_string(tolower(c) - 'a' + 1) + " "; // kalau ada, konversi karakter c ke posisinya sesuai urutan alphabet
        }
    }
    // hapus spasi di akhir temp bila ada
    if(!temp.empty()){
        temp.pop_back();
    }
    return temp;
}


// Sample test
/*
Describe(Sample_Tests) {
  It(Tests) {
    Assert::That(alphabet_position("The sunset sets at twelve o' clock."), Equals("20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"));
    Assert::That(alphabet_position("The narwhal bacons at midnight."), Equals("20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20"));
    Assert::That(alphabet_position("0123456789"), Equals(""));
    Assert::That(alphabet_position(",./<>?-_=+ "), Equals(""));
    Assert::That(alphabet_position(""), Equals(""));
  }
};
*/




/*
PERFECT SOLUTION FROM CODEWARS

=1=
#include <string>

std::string alphabet_position(const std::string &text) {
  std::string str1;
    int d=text.length();
    char ch;
    std::string word;
                        
    for(int i=0; i<d; i++) {
        ch = text[i]; 
        switch(ch) {
            case 'a':
            case 'A':
                word = "1";
                break;
            case 'b':
            case 'B':
                word = "2";
                break;
            case 'c':
            case 'C':
                word = "3";
                break;
            case 'd':
            case 'D':
                word = "4";
                break;
            case 'e':
            case 'E':
                word = "5";
                break;
            case 'f':
            case 'F':
                word = "6";
                break;
            case 'g':
            case 'G':
                word = "7";
                break;
            case 'h':
            case 'H':
                word = "8";
                break;
            case 'i':
            case 'I':
                word = "9";
                break;
            case 'j':
            case 'J':
                word = "10";
                break;
            case 'k':
            case 'K':
                word = "11";
                break;
            case 'l':
            case 'L':
                word = "12";
                break;
            case 'm':
            case 'M':
                word = "13";
                break;
            case 'n':
            case 'N':
                word = "14";
                break;
            case 'o':
            case 'O':
                word = "15";
                break;
            case 'p':
            case 'P':
                word = "16";
                break;
            case 'q':
            case 'Q':
                word = "17";
                break;
            case 'r':
            case 'R':
                word = "18";
                break;
            case 's':
            case 'S':
                word = "19";
                break;
            case 't':
            case 'T':
                word = "20";
                break;
            case 'u':
            case 'U':
                word = "21";
                break;    
            case 'v':
            case 'V':
                word = "22";
                break;    
            case 'w':
            case 'W':
                word = "23";
                break;    
            case 'x':
            case 'X':
                word = "24";
                break;    
            case 'y':
            case 'Y':
                word = "25";
                break;    
            case 'z':
            case 'Z':
                word = "26";
                break;        
        }

        if(!((ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z'))) {
            continue;
    }  
        else          
            str1 += word + " ";        
        } 
     if(str1 != "")
        str1.erase(str1.length()-1);  
         
    return str1; 
}



=2=
#include <string>

using namespace std;

std::string alphabet_position(const std::string &text) {
  string res = "";
  
  for (char c : text) {
    c = tolower(c);
    if ('a' <= c && c <= 'z') {
      if (res != "") {
        res += " ";
      }
      res += to_string(c - 'a' + 1);
    }
  }
  
  return res;
}


=3=
#include <string>

std::string alphabet_position(const std::string &text) {
  std::string result = "";
  for (size_t i = 0; i < text.size(); i++) {
    char c = text[i];
    if (std::isalpha(c)) {
      if (!result.empty())
        result += " ";
      result += std::to_string(std::toupper(c) - 64);
    }
  }
  
  return result;
}


=4=
#include <string>
#include <string.h>

std::string alphabet_position(const std::string& text) {
	const char* c_str = text.c_str();
	std::string result;
	for (int i = 0; i < (int)strlen(c_str); i++) {
		if (isalpha(c_str[i])) {
			if (result != "")
				result += " ";
			result += std::to_string((int)tolower(c_str[i]) - 96);
		}
	}
	return result;
}


=5=
#include <iostream>
#include <string>
using namespace std;

string alphabet_position(const string &text)
{
    string sAlphabet = "abcdefghijklmnopqrstuvwxyz";
    string bAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    string result = "";
    for (char c : text)
    {
        if ((c >= 'a' && c <= 'z'))
        {
            result += to_string(sAlphabet.find(c) + 1) + " ";
        }
        if ((c >= 'A' && c <= 'Z'))
        {
            result += to_string(bAlphabet.find(c) + 1) + " ";
        }
    }
    return result.substr(0, result.size() - 1);
}
*/