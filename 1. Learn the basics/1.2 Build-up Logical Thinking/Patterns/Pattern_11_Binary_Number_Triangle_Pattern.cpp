/*
Q. Given an integer N, print the following pattern.

Input Format: N = 3
Result: 
1
01
101

Input Format: N = 6
Result:   
1
01
101
0101
10101
010101

Explaination :  track row and column with 2 bool variable
another approach column (for even 0 and for odd 1) and print values in inner loop alternatively
*/

#include <bits/stdc++.h>
using namespace std;

void pattern11(int n){
    bool row = 1;
    bool column = 1;
    for(int i=1; i<=n; i++){
        for(int j=1; j<=i; j++){
            cout << row;
            row = !row;
        }
        cout << endl;
        column = !column;
        row = column;
    }
}


int main(){
    int n;
    cin >> n;
    pattern11(n);
    return 0;
}