/*
Q. Given an integer N, print the following pattern.

Input Format: N = 3
Result: 
1    1
12  21
123321

Input Format: N = 6
Result:   
1          1
12        21
123      321
1234    4321
12345  54321
123456654321

Explaination :  number, space, number
1               [1, 4, 1]
2               [12, 2, 21]
3               [123, 0, 321]
                [i, 2*(n-i), i]
*/

#include <bits/stdc++.h>
using namespace std;

void pattern12(int n){
    for(int i=1; i<=n; i++){
        for(int j=1; j<=i; j++)
            cout << j;
        for(int k=1; k<=2*(n-i); k++)
            cout << " ";
        for(int j=i; j>=1; j--)
            cout << j;
        cout << endl;
    }
}


int main(){
    int n;
    cin >> n;
    pattern12(n);
    return 0;
}