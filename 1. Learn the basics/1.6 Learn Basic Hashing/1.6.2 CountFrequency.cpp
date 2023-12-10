#include <bits/stdc++.h>
using namespace std;
/*
Q. Given an array, we have found the number of occurrences of each element in the array.

Example 1:
Input: arr[] = {10,5,10,15,10,5};
Output: 10  3
	 5  2
        15  1
Explanation: 10 occurs 3 times in the array
	      5 occurs 2 times in the array
              15 occurs 1 time in the array

Example2: 
Input: arr[] = {2,2,3,4,4,2};
Output: 2  3
	3  1
        4  2
Explanation: 2 occurs 3 times in the array
	     3 occurs 1 time in the array
             4 occurs 2 time in the array

*/

void frequencyCount(vector<int> &arr, int N){
    int temp[N+1] = {0};
    for(int i=0;i<=N;i++){
        temp[arr[i]] ++;
    }

    for(int i=0;i<N;i++){
        cout << arr[i] << " occurs "<< temp[arr[i]] << " times" << endl;
    }
}

void frequencyCountUsingMap(vector<int> &arr, int N){
    map<int, int> frequency;

    for(int i=0; i<N; i++){
        frequency.insert(arr[i], frequency[arr[i]++]);
    }

    for(auto freq: frequency){
        cout << freq.first << " occurs" << freq.second << " times" << endl;
    }
}

int main(){
    vector<int> arr={2,3,3,2,5};
    int N = 5;
    frequencyCountUsingMap(arr, N);
    return 0;
}


/*
Complexity : Time => O(N), Space => O(N+1)

Dry Run

arr = [2,3,3,2,5]

 i         temp
 0     [0,1,0,0,0]
 1     [0,1,1,0,0]
 2     [0,1,2,0,0]
 3     [0,1,2,0,0]
 4     [0,2,2,0,0]
 5     [0,2,2,0,1]

*/