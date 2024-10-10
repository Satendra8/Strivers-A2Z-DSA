/*
Q. Given an integer N, print the following pattern.

Input Format: N = 3
Result: 
  *  
 ***
***** 
*****  
 ***
  *   
Input Format: N = 6
Result:   
     *
    ***
   ***** 
  *******
 *********
***********  
***********
 *********
  *******
   ***** 
    ***    
     *

Explaination :  
First Half
                space, stars, space
1               [2, 1, 2]
2               [1, 3, 1]
3               [0, 5, 0]
                [n-i, 2*i-1, n-i]

Second Half
                space, stars, space
1               [0, 5, 0]
2               [1, 3, 1]
3               [2, 1, 2]
                [i-1, 2*(n-i)+1, i-1]

*/

#include <bits/stdc++.h>
using namespace std;

void pattern9(int n){
    for(int i=1; i<=n; i++){
        for(int j=1; j<=n-i; j++)
            cout << " ";
        for(int j=1; j<=2*i-1; j++)
            cout << "*";

        cout << endl;
    }
    for(int i=1; i<=n; i++){
        for(int j=1; j<=i-1; j++)
            cout << " ";
        for(int j=1; j<=2*(n-i)+1; j++)
            cout << "*";

        cout << endl;
    }
}


int main(){
    int n;
    cin >> n;
    pattern9(n);
    return 0;
}