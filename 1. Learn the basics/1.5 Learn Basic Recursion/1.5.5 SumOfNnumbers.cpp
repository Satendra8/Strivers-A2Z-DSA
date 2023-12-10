#include <bits/stdc++.h>
using namespace std;
/*
Q. Given a number ‘N’, find out the sum of the first N natural numbers.

Example 1:
Input: N=5
Output: 15
Explanation: 1+2+3+4+5=15

5 + 10
4 + 6
3 + 3
2 + 1
1


Example 2:
Input: N=6
Output: 21
Explanation: 1+2+3+4+5+6=15

*/

int sumOfNumbers(int N){
    if(N==1){
        return 1;
    }
    return (N + sumOfNumbers(N-1));
    // 5 + sum(4) + sum(3) + sum(2) + sum(1)
}

int main(){
    cout << "Enter a Number ";
    int N;
    cin >> N;
    // cout << "Sum is " << sumOfNumbers(N);
    int s = sumOfNumbers(N);
    cout << "sum is " << s;
    return 0;
}