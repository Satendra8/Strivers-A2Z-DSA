/*
Q. Given an integer N, print the following pattern.

Input Format: N = 3
Result: 
C
B C
A B C

Input Format: N = 6
Result:   
F
E F
D E F
C D E F
B C D E F
A B C D E F

Explaination : letter (start with 65+N)
0                  C
1                  B C
2                  A B C
                   (ch-j)
*/

#include <bits/stdc++.h>
using namespace std;

void pattern18(int n){
    char ch = 'A' + n-1;
    for(int i=0; i<n; i++){
        for(int j=i; j>=0; j--){
            cout << char(ch - j) << " ";
        }
        cout << endl;
    }
}


int main(){
    int n;
    cin >> n;
    pattern18(n);
    return 0;
}