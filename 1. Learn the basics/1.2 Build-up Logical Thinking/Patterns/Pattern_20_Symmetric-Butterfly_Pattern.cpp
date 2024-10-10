/*
Q. Given an integer N, print the following pattern.

Input Format: N = 3
Result: 
*    *
**  **
******
**  **
*    *


Input Format: N = 6
Result:   
*          *
**        **
***      ***
****    ****
*****  *****
************
*****  *****
****    ****
***      ***
**        **
*          *

Explaination : star space star
1               1     4     1
2               2     2     2
3               3     0     3
              (i,n) (2*(n-i)) (i,n)                    reverse
4               2     2     2
5               1     4     1
            (2*n-i) (2(i-n)) (2*n-i)

*/

#include <bits/stdc++.h>
using namespace std;

void pattern20(int n){
    for(int i=1; i<2*n; i++){
        if(i<=n){
            for(int j=1; j<=i; j++){
                cout << "*";
            }

            for(int j=1; j<=2*(n-i); j++){
                cout << " ";
            }

            for(int j=1; j<=i; j++){
                cout << "*";
            }
        }
        else{
            for(int j=1; j<=2*n-i; j++){
                cout << "*";
            }

            for(int j=1; j<=2*(i-n); j++){
                cout << " ";
            }

            for(int j=1; j<=2*n-i; j++){
                cout << "*";
            }
        }
        cout << endl;
    }
}


int main(){
    int n;
    cin >> n;
    pattern20(n);
    return 0;
}