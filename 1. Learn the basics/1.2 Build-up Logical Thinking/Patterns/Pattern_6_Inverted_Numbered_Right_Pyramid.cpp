/*
Q. Given an integer N, print the following pattern.

Input Format: N = 3
Result: 
1 2 3
1 2
1

Input Format: N = 6
Result:
1 2 3 4 5 6
1 2 3 4 5
1 2 3 4
1 2 3
1 2 
1

Explaination :  1st-row numbers from 1 to N get printed, in the 2nd-row numbers from 1 to (N-1) get printed, and so on.

*/

#include <bits/stdc++.h>
using namespace std;

void pattern6(int n){
    for(int i=n; i>=1; i--){
        for(int j=1; j<=i; j++){
            cout << j << " ";
        }
        cout << endl;
    }
}


int main(){
    int n;
    cin >> n;
    pattern6(n);
    return 0;
}