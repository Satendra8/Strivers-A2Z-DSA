#include <bits/stdc++.h>
using namespace std;
/*
Q. Given a string, check if the string is palindrome or not.”  A string is said to be palindrome if the reverse of the string is the same as the string.

Example 1:
Input: Str =  “ABCDCBA”
Output: Palindrome
Explanation: String when reversed is the same as string.

Example 2:
Input: Str = “TAKE U FORWARD”
Output: Not Palindrome
Explanation: String when reversed is not the same as string.

*/

bool checkPalindrom(string S, int start, int end){
    if(start >= end){
        return true;
    }
    if(S[start] == S[end]){
        return checkPalindrom(S, start+1, end-1);
    }
    else
        return false;
}

int main(){
    string S;
    cout << "Enter a String :" ;
    cin >> S;
    int l = S.length();
    bool result = checkPalindrom(S, 0, l-1);
    if(result)
        cout << "Palindrom";
    else
        cout << "Not Palindrom";
    return 0;
}


/*
Dry Run
Input: Str =  “ABCDCBA”

start  end      value
  0     6       A==A
  1     5       B==B     
  2     4       C==C
  3     3         D

*/