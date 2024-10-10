#include<bits/stdc++.h>
using namespace std;

/*
Q. Find the gcd of two numbers.

Example 1:
Input: num1 = 4, num2 = 8
Output: 4
Explanation: Since 4 is the greatest number which divides both num1 and num2.

Example 2:
Input: num1 = 3, num2 = 6
Output: 3
Explanation: Since 3 is the greatest number which divides both num1 and num2.

*/

void lcmAndGcdNaive(long long A, long long B){
    // GCD Complexty O(n)
    long long temp;
    if(A > B){
        temp = A;
        A = B;
        B = temp;
    }
    for(int i=A; i>=1; i--){
        if(A%i == 0 && B%i == 0){
            cout << "GCD is : " << i << endl;
            return;
        }
    }
    // LCM Complexty O(n)
    for(int i=B; i<=A*B; i++){
        if(i%B == 0 && i%A == 0){
            cout << "LCM is : " << i << endl;
            return;
        }
    }
    cout << "GCD is : " << 1 << endl;
    return;
}

vector<long long> lcmAndGcd(long long A , long long B) {
    // code here
    long long temp, multiply;
    vector <long long> result;
    multiply = A*B;

    if(A > B){
        temp = A;
        A = B;
        B = temp;
    }
    while(B%A != 0){
        long long rem = B%A;
        B = A;
        A = rem;
    }
    result.push_back(multiply/A);
    result.push_back(A);
    return result;
}

int main(){
    int A, B;
    cout << "Enter two Numbers :" ;
    cin >> A >> B;
    // lcmAndGcdNaive(A, B);
    lcmAndGcd(A, B);
    return 0;
}



/*
Explanation : 

Approach 1 : naive method
Complexity : O(n)

Approach 2 : Using Euclidean’s theorem. gcd(a,b) = gcd(b,a%b)
Complexity : O(logɸmin(a,b)), where ɸ is 1.61.

*/