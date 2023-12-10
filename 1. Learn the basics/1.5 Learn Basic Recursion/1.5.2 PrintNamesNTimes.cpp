#include <bits/stdc++.h>
using namespace std;
/*
Q. Print your Name N times using recursion.
*/

void printName(int curr, int N){
    if(curr==N){
        return;
    }
    cout << "Satendra" << endl;
    printName(++curr, N);
    return;
}

int main(){
    cout << "Enter a Number ";
    int N;
    cin >> N;
    printName(0, N);
    return 0;
}