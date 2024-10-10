#include <bits/stdc++.h>
using namespace std;
/*
Q. You are given an array. The task is to reverse the array and print it.

Example 1:
Input: N = 5, arr[] = {5,4,3,2,1}
Output: {1,2,3,4,5}
Explanation: Since the order of elements gets reversed the first element will occupy the fifth position, the second element occupies the fourth position and so on.

Example 2:
Input: N=4 arr[] = {10,20,30,40}
Output: {40,30,20,10}
Explanation: Since the order of elements gets reversed the first element will occupy the fifth position, the second element occupies the fourth position and so on.

*/

void printArray(int arr[], int N){
    for(int i=0; i<N; i++){
        cout << arr[i] << " ";
    }
    cout << endl;
}

void reverseAnArray(int arr[], int start, int end){
    if(start>=end) return;
    swap(arr[start], arr[end]);
    reverseAnArray(arr, ++start, --end);
    return;
}

int main(){
    int N;
    cout << "Enter a Number :" ;
    cin >> N;
    int arr[N];
    cout << "Enter Array Elements : ";
    for(int i=0; i<N; i++)
        cin >> arr[i];
    reverseAnArray(arr, 0, N-1);
    printArray(arr, N);
    return 0;
}


/*
Dry Run
Input: N = 5, arr[] = {5,4,3,2,1}

start  end      array
  0     4     1 4 3 2 5
  1     3     1 2 3 4 5
  2     2     1 2 3 4 5

*/