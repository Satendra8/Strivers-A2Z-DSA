#include <bits/stdc++.h>
using namespace std;
/*
Q. Print from 1 to N using Recursion.
*/

void printNumber(int curr, int N){
    if(curr==N){
        return;
    }
    cout << ++curr << endl;
    printNumber(curr, N);
    return;
}

int main(){
    cout << "Enter a Number ";
    int N;
    cin >> N;
    printNumber(0, N);
    return 0;
}