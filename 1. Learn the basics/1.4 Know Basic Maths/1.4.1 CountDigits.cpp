/*
Q. Given an integer N, write a program to count the number of digits in N.

Example 1:
Input: N = 12345
Output: 5
Explanation: N has 5 digits

Example 2:
Input: N = 8394
Output: 4
Explanation: N has 4 digits

*/

#include <bits/stdc++.h>
using namespace std;


// Approach 1
void CountDigit1(int n){
    int counter = 0;
    while(n>0){
        n=n/10;
        counter++;
    }
    cout << "Digit Count is: " << counter;
}

// Approach 2
void CountDigit2(int n){
    string digit = to_string(n);
    cout << "Count is: " << digit.length();
}


// Approach 3
void CountDigit3(int n){
    int counter = log10(n) + 1;
    cout << "Count is: " << counter;
}

int main(){
    int n;
    cin >> n;
    CountDigit3(n);
    return 0;
}




/*
Explanation : 

Approach 1 : Divide by 10  till 0 and count iteration
Complexity : O(n) where n is number of digit

Approach 2 : make string and get the length
Complexity : O(1)

Approach 3 : use log with base 10 to get count
Complexity : O(1)

*/