/*
Q. Given an integer N, print the following pattern.

Input Format: N = 3
Result: 
***
* *
***

Input Format: N = 6
Result:   
******
*    *
*    *
*    *
*    *
******

Explaination : star space star
1               2     0     1
2               1     1     1
3               2     0     1
print * only when i, j, n

*/

#include <bits/stdc++.h>
using namespace std;

void pattern21(int n){
    for(int i=1; i<=n; i++){
        for(int j=1; j<=n; j++){
            if(i==1 || j==1 || i==n || j== n)
                cout << "*";
            else
                cout << " ";
        }
        cout << endl;
    }
}


int main(){
    int n;
    cin >> n;
    pattern21(n);
    return 0;
}