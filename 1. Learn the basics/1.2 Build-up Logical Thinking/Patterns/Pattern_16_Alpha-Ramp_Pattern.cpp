/*
Q. Given an integer N, print the following pattern.

Input Format: N = 3
Result: 
A
B B
C C C

Input Format: N = 6
Result:   
A 
B B
C C C
D D D D
E E E E E
F F F F F F

Explaination : start with 65
*/

#include <bits/stdc++.h>
using namespace std;

void pattern16(int n){
    char ch = 'A';
    for(int i=0; i<n; i++){
        for(int j=0; j<=i; j++){
            cout << char(ch + i) << " ";
        }
        cout << endl;
    }
}


int main(){
    int n;
    cin >> n;
    pattern16(n);
    return 0;
}