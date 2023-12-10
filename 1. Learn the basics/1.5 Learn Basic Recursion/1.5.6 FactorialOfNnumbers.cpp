#include <bits/stdc++.h>
using namespace std;
/*
Q. Given a number X,  print its factorial.

Example 1:
Input: X = 5
Output: 120
Explanation: 5! = 5*4*3*2*1

Example 2:
Input: X = 3
Output: 6
Explanation: 3!=3*2*1

*/

int factorial(int N){
    if(N==0){
        return 1;
    }
    return N * factorial(N-1);
}

int main(){
    cout << "Enter a Number ";
    int N;
    cin >> N;
    cout << "Factorial is " << factorial(N);
    return 0;
}