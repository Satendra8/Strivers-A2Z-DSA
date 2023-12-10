/*
Q. Given an integer N, print the following pattern.

Input Format: N = 3
Result: 
1
2 2 
3 3 3

Input Format: N = 6
Result:
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
6 6 6 6 6 6

Explaination :  1 number for row 1, 5 numbers for row 5, and so on.

*/

#include <bits/stdc++.h>
using namespace std;

void pattern4(int n){
    for(int i=1; i<=n; i++){
        for(int j=1; j<=i; j++){
            cout << i << " ";
        }
        cout << endl;
    }
}


int main(){
    int n;
    cin >> n;
    pattern4(n);
    return 0;
}