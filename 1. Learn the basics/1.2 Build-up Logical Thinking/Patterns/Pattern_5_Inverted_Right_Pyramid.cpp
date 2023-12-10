/*
Q. Given an integer N, print the following pattern.

Input Format: N = 3
Result: 
* * *
* * 
*

Input Format: N = 6
Result:
* * * * * *
* * * * * 
* * * * 
* * * 
* * 
* 

Explaination :  Row 1 (i=0) would contain N stars, Row 2 (i=1) would contain (N -1) stars and so on.

*/

#include <bits/stdc++.h>
using namespace std;

void pattern5(int n){
    for(int i=1; i<=n; i++){
        for(int j=n; j>=i; j--){
            cout << "* ";
        }
        cout << endl;
    }
}


int main(){
    int n;
    cin >> n;
    pattern5(n);
    return 0;
}