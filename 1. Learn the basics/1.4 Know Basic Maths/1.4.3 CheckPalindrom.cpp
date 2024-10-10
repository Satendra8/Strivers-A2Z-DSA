#include <bits/stdc++.h>
using namespace std;


/*
 * Q. Write a program to check whether a given string is palindrome or not.
 * Example:
 * input: str = "malylam"
 * output: 1
 * 
 * Example:
 * input: str = "manish"
 * output: 0
 */


/* Iterative method */

string checkPalindrom1(string S){
    string res = "";
    cout << "size :" << S.size() << endl; 
    for(int i=S.size()-1; i>=0; i--){
        res += S[i];
    }
    if(S == res) cout << "Palindrom";
    else cout << "Not Palindrom";
    return res;
}


/* Recursive method */

int checkPalindrom2(int index, string S){
    int N = S.size();
    // cout << "N: " << N << endl;
    if(index >= N/2) return 1;

    // cout << S[index] << " " << S[N-(index+1)] << endl;
    if (S[index] == S[N-(index+1)]){
        return checkPalindrom2(++index, S);
    }
    else
        return 0;
}

int main(){
    string S;
    cout << "Enter a String : "<< endl;
    cin >> S;
    cout << checkPalindrom2(0, S) << endl;
    return 0;
}


/*
Explanation : 

Approach 1 : Iterative method
Complexity : O(n) where n is number of digit

Approach 2 : Recursive method

abba (even length)
check first and last element and repeates the same.

abbcbba (odd length)
1. a==a
2. b==b
3. b==b
4. c

*/