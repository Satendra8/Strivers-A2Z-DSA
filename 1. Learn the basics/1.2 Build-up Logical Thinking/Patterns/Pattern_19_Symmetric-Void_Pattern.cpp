/*
Q. Given an integer N, print the following pattern.

Input Format: N = 3
Result: 
******
**  **
*    *
*    *
**  **
******

Input Format: N = 6
Result:   
************
*****  *****
****    ****
***      ***
**        **
*          *
*          *
**        **
***      ***
****    ****
*****  *****
************

Explaination : star space star
1               3     0     3
2               2     2     2
3               1     4     1
              (i,n) (2*i-2) (i,n)                    reverse
1               1     4     1
2               2     2     2
3               3     0     3
            (1, i) (2(n-i)) (1, i)

*/

#include <bits/stdc++.h>
using namespace std;

void pattern19(int n){
    for(int i=1; i<=n; i++){
        for(int j=i; j<=n; j++){
            cout << "*";
        }
        for(int j=1; j<=2*i-2; j++){
            cout << " ";
        }
        for(int j=i; j<=n; j++){
            cout << "*";
        }
        cout << endl;
    }
    for(int i=1; i<=n; i++){
        for(int j=1; j<=i; j++){
            cout << "*";
        }
        for(int j=1; j<=2*(n-i); j++){
            cout << " ";
        }
        for(int j=1; j<=i; j++){
            cout << "*";
        }
        cout << endl;
    }
}


int main(){
    int n;
    cin >> n;
    pattern19(n);
    return 0;
}