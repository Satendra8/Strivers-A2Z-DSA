/*
Q. Given an integer N, print the following pattern.

Input Format: N = 3
Result: 
1
1 2 
1 2 3

Input Format: N = 6
Result:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6

Explaination :  1 number for row 1, 5 numbers for row 5, and so on.

*/

#include <bits/stdc++.h>
using namespace std;

void pattern3(int n){
    for(int i=1; i<=n; i++){
        for(int j=1; j<=i; j++){
            cout << j << " ";
        }
        cout << endl;
    }
}


int main(){
    int n;
    cin >> n;
    pattern3(n);
    return 0;
}