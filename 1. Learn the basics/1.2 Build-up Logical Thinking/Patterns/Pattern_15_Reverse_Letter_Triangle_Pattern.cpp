/*
Q. Given an integer N, print the following pattern.

Input Format: N = 3
Result: 
A B C
A B
A

Input Format: N = 6
Result:   
A B C D E F
A B C D E 
A B C D
A B C
A B
A

Explaination : start with 65
*/

#include <bits/stdc++.h>
using namespace std;

void pattern15(int n){
    char ch = 'A';
    for(int i=0; i<n; i++){
        for(int j=0; j<=(n-i); j++){
            cout << char(ch + j) << " ";
        }
        cout << endl;
    }
}


int main(){
    int n;
    cin >> n;
    pattern15(n);
    return 0;
}