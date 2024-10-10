/*
Q. Given an integer N, print the following pattern.

Input Format: N = 3
Result: 
  A  
 ABA 
ABCBA


Input Format: N = 6
Result:   
     A     
    ABA    
   ABCBA   
  ABCDCBA  
 ABCDEDCBA 
ABCDEFEDCBA

Explaination : space letter
0               2       A
1               1       ABA
2               0       ABCBA
                (i, n)  (i,n)(n,i)
*/

#include <bits/stdc++.h>
using namespace std;

void pattern17(int n){
    char ch = 'A';
    for(int i=0; i<n; i++){
        for(int j=i; j<n-1; j++){
            cout << " ";
        }
        for(int j=0; j<=i; j++){
            cout << char(ch+j);
        }
        for(int j=i-1; j>=0; j--){
            cout << char(ch+j);
        }
        cout << endl;
    }
}


int main(){
    int n;
    cin >> n;
    pattern17(n);
    return 0;
}