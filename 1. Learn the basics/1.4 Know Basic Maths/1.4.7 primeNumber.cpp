#include<bits/stdc++.h>
using namespace std;

/*
Q. Given a number, check whether it is prime or not. A prime number is a natural number that is only divisible by 1 and by itself.

Example 1:
Input: N = 3
Output: Prime
Explanation: 3 is a prime number

Example 2:
Input: N = 26
Output: Non-Prime
Explanation: 26 is not prime

*/

// naive approach
void primeNumber1(int N){
    if(N==0){
       cout << "Non-Prime";
       return; 
    }
    if(N<=2){
        cout << "Prime";
        return;
    }
    for(int i=2; i<N; i++){
        if(N%i==0){
            cout << "Non-Prime";
            return;
        }
    }
    cout << "Prime";
    return;
}

// optimal approach
void primeNumber2(int N){
   if(N==0){
       cout << "Non-Prime";
       return; 
    }
    if(N<=2){
        cout << "Prime";
        return;
    }
    for(int i=2; i<=sqrt(N); i++){
        if(N%i==0){
            cout << "Non-Prime";
            return;
        }
    }
    cout << "Prime";
    return;
}

int main(){
    int N;
    cout << "Enter a Number :" ;
    cin >> N;
    primeNumber2(N);
    return 0;
}

/*
Explanation : 

Approach 1 : iterate from 2 to N
Complexity : O(n)

Approach 2 : iterate from 2 to sqrt(n)
Complexity : O(sqrt(n))

*/