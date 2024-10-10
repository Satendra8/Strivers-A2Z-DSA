/*
Q. Given an integer N, print the following pattern.

Input Format: N = 3
Result: 
1
2 3
4 5 6

Input Format: N = 6
Result:   
1
2  3
4  5  6
7  8  9  10
11  12  13  14  15
16  17  18  19  20  21

Explaination :  number   and initilize a counter
                [1 to i]
*/

#include <bits/stdc++.h>
using namespace std;

void pattern13(int n){
    int counter = 1;
    for(int i=1; i<=n; i++){
        for(int j=1; j<=i; j++){
            cout << counter << " ";
            counter++;
        }
        cout << endl;
    }
}


int main(){
    int n;
    cin >> n;
    pattern13(n);
    return 0;
}