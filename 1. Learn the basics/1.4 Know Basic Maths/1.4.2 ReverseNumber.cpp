/*
Q. Given an integer N, write a program to count the number of digits in N.

Example 1:
Input: N = 123
Output: 321
Explanation: The reverse of 123 is 321

Example 2:
Input: N = 234
Output: 432
Explanation: The reverse of 234 is 432

*/

#include <bits/stdc++.h>
using namespace std;


void ReverseNumber(int n){
    int reversedNumber = 0;

    while(n>0){
        int current = n%10;
        reversedNumber = current + reversedNumber*10;
        n = n/10;
    }
    cout << "Reverse Number is: " << reversedNumber;
}



int main(){
    int n;
    cin >> n;
    ReverseNumber(n);
    return 0;
}




/*
Explanation : 

Approach : Divide by 10  till 0 and current + reversedNumber*10;
Complexity O(n)

*/