#include <bits/stdc++.h>
using namespace std;
/*
Q. Given an integer N. Print the Fibonacci series up to the Nth term.

Example 1:
Input: N = 5
Output: 0 1 1 2 3 5
Explanation: 0 1 1 2 3 5 is the fibonacci series up to 5th term.(0 based indexing)

Example 2:
Input: 6

Output: 0 1 1 2 3 5 8
Explanation: 0 1 1 2 3 5 8 is the fibonacci series upto 6th term.(o based indexing)

*/

int printFibonacci(int N){
    if(N<=1){
        return N;
    }
    return (printFibonacci(N-1) + printFibonacci(N-2));
}

int main(){
    int N;
    cout << "Enter a Number :" ;
    cin >> N;
    cout << printFibonacci(N) << " ";
    return 0;
}


/*
Complexity O(2^N)
Dry Run
Input: N = 5

I will be uploading it.
*/