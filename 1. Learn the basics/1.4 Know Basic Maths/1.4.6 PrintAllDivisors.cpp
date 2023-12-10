#include<bits/stdc++.h>
using namespace std;

/*
Q. Given a number, print all the divisors of the number. A divisor is a number that gives the remainder as zero when divided.

Example 1:
Input: n = 36
Output: 1 2 3 4 6 9 12 18 36
Explanation: All the divisors of 36 are printed.

Example 2:
Input: n = 97
Output: 1 97
Explanation: Since 97 is a prime number, only 1 and 97 are printed.

*/

// naive approach
void printAllDivisors1(int N){
    for(int i=1; i<=N; i++){
        cout << i << " ";
    }
    return;
}

// optimal approach
void printAllDivisors2(int N){
    // 1, 36, 2, 18, 3, 12, 4, 9, 6
    for(int i=1; i<=sqrt(N); i++){
        if(N%i==0){
            cout << i << " ";
            if(sqrt(N) != i)
                cout << N/i << " ";
        }
    }
    return;
}

int main(){
    int N;
    cout << "Enter a Number :" ;
    cin >> N;
    printAllDivisors2(N);
    return 0;
}

/*
Explanation : 

Approach 1 : iterate from 1 to N
Complexity : O(n)

Approach 2 : iterate from 1 to sqrt(n)
Complexity : O(sqrt(n))

*/