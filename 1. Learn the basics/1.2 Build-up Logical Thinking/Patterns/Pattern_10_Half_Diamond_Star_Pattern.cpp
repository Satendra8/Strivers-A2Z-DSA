/*
Q. Given an integer N, print the following pattern.

Input Format: N = 3
Result: 
  *  
  **
  ***  
  **
  *   
Input Format: N = 6
Result:   
    *
    **
    *** 
    ****
    *****
    ******  
    *****
    ****
    ***    
    **
    *

Explaination :  
                stars
1               [i]
2               [i]
3               [i]
4               [2*n - i]
5               [2*n - i]

*/

#include <bits/stdc++.h>
using namespace std;

void pattern10(int n){
    for(int i=1; i<2*n; i++){
        if(i<=n){
            for(int j=1; j<=i; j++)
                cout << "*";
        }
        else{
            for(int j=1; j<=2*n - i; j++)
                cout << "*";
        }

        cout << endl;
    }
}


int main(){
    int n;
    cin >> n;
    pattern10(n);
    return 0;
}