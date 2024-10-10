/*
Q. Given an integer N, print the following pattern.

Input Format: N = 3
Result: 
3 3 3 3 3 
3 2 2 2 3 
3 2 1 2 3 
3 2 2 2 3 
3 3 3 3 3

Input Format: N = 6
Result:   
6 6 6 6 6 6 6 6 6 6 6 
6 5 5 5 5 5 5 5 5 5 6 
6 5 4 4 4 4 4 4 4 5 6 
6 5 4 3 3 3 3 3 4 5 6 
6 5 4 3 2 2 2 3 4 5 6 
6 5 4 3 2 1 2 3 4 5 6 
6 5 4 3 2 2 2 3 4 5 6 
6 5 4 3 3 3 3 3 4 5 6 
6 5 4 4 4 4 4 4 4 5 6 
6 5 5 5 5 5 5 5 5 5 6 
6 6 6 6 6 6 6 6 6 6 6

Explaination : find the minimum distance from right, left, top, bottom (run i and j < 2*n-1)

Eg: n=3

0 0 0 0 0      3 3 3 3 3
0 1 1 1 0      3 2 2 2 3
0 1 2 1 0  =>  3 2 1 2 3
0 1 1 1 0      3 2 2 2 3
0 0 0 0 0      3 3 3 3 3

Eg: n=6

0 0 0 0 0 0 0 0 0 0 0       6 6 6 6 6 6 6 6 6 6 6
0 1 1 1 1 1 1 1 1 1 0       6 5 5 5 5 5 5 5 5 5 6
0 1 2 2 2 2 2 2 2 1 0       6 5 4 4 4 4 4 4 4 5 6
0 1 2 3 3 3 3 3 2 1 0       6 5 4 3 3 3 3 3 4 5 6
0 1 2 3 4 4 4 3 2 1 0       6 5 4 3 2 2 2 3 4 5 6
0 1 2 3 4 5 4 3 2 1 0   =>  6 5 4 3 2 1 2 3 4 5 6
0 1 2 3 4 4 4 3 2 1 0       6 5 4 3 2 2 2 3 4 5 6
0 1 2 3 3 3 3 3 2 1 0       6 5 4 3 3 3 3 3 4 5 6
0 1 2 2 2 2 2 2 2 1 0       6 5 4 4 4 4 4 4 4 5 6
0 1 1 1 1 1 1 1 1 1 0       6 5 5 5 5 5 5 5 5 5 6
0 0 0 0 0 0 0 0 0 0 0       6 6 6 6 6 6 6 6 6 6 6

*/

#include <bits/stdc++.h>
using namespace std;

void pattern22(int n){
    int left = 0, right=2*n-2, top=0, bottom=2*n-2; 
    for(int i=0; i<2*n-1; i++){
        for(int j=0; j<2*n-1; j++){
            // for [i=2, j=2]  (2, ((2, 2), 2))
            // for [i=7, j=3]  (3, ((7, 7), 3))
            cout << n - min(j-left, min(min(i-top, right-j), bottom-i)) << " ";
        }
        cout << endl;
    }
}


int main(){
    int n;
    cin >> n;
    pattern22(n);
    return 0;
}