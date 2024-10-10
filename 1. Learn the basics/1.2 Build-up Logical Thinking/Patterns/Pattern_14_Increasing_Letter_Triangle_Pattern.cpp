/*
Q. Given an integer N, print the following pattern.

Input Format: N = 3
Result: 
A
A B
A B C

Input Format: N = 6
Result:   
A
A B
A B C
A B C D
A B C D E
A B C D E F

Explaination : start with 65
*/

#include <bits/stdc++.h>
using namespace std;

void pattern14(int n){
    char ch = 'A';
    for(int i=0; i<n; i++){
        for(int j=0; j<=i; j++){
            cout << char(ch + j) << " ";
        }
        cout << endl;
    }
}


int main(){
    int n;
    cin >> n;
    pattern14(n);
    return 0;
}