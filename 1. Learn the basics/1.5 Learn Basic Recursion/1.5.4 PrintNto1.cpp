#include <bits/stdc++.h>
using namespace std;
/*
Q. Print from N to 1 using Recursion.
*/

void printNumber(int N){
    if(N==0){
        return;
    }
    cout << N << endl;
    printNumber(--N);
    return;
}

int main(){
    cout << "Enter a Number ";
    int N;
    cin >> N;
    printNumber(N);
    return 0;
}