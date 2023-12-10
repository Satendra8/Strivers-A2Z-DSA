/*
Q. Given an integer N, print the following pattern.

Input Format: N = 3
Result: 
* 
* * 
* * *

Input Format: N = 6
Result:
* 
* * 
* * *
* * * *
* * * * *
* * * * * *

Explaination :  1 star for row 1, 5 stars for row 5, and so on.

*/

#include <bits/stdc++.h>
using namespace std;

void pattern2(int n){
    for(int i=1; i<=n; i++){
        for(int j=1; j<=i; j++){
            cout << "* ";
        }
        cout << endl;
    }
}


int main(){
    int n;
    cin >> n;
    pattern2(n);
    return 0;
}