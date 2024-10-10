#include<bits/stdc++.h>
using namespace std;

/*
Q. Given a number, check if it is Armstrong Number or Not.

Example 1:
Input:153 
Output: Yes, it is an Armstrong Number
Explanation: 1^3 + 5^3 + 3^3 = 153

Input:170 
Output: No, it is not an Armstrong Number
Explanation: 1^3 + 7^3 + 0^3 != 170

Input:1634 
Output: Yes, it is an Armstrong Number
Explanation: 1^4 + 6^6 + 3^4 + 4^4 = 1634

*/

void checkArmstrong(int n){
    int temp = n;
    int sum = 0;

    int lenght = (to_string(n)).length();
    while(n>0){
        int digit = n%10;
        sum = sum + pow(digit, lenght);
        n=n/10;
    }

    if(temp == sum)
        cout<< temp << " is Armstrong";
    else
        cout<< temp << " is Not Armstrong";
    return;
}

int main(){
    int n;
    cin >> n;
    checkArmstrong(n);
    return 0;
}


/*
Explanation : 

Approach 1 : iterate over digits.
Complexity : O(n) where n is number of digit.

*/