#include <bits/stdc++.h>
using namespace std;
/*
Q. Given an array of size N. Find the highest and lowest frequency element.

Example 1:
Input: array[] = {10,5,10,15,10,5};
Output: 10 15
Explanation: The frequency of 10 is 3, i.e. the highest and the frequency of 15 is 1 i.e. the lowest.

Example 2:

Input: array[] = {2,2,3,4,4,2};
Output: 2 3
Explanation: The frequency of 2 is 3, i.e. the highest and the frequency of 3 is 1 i.e. the lowest.

*/

void findHighestAnLowestFrequency(vector<int> &arr, int N){
    map<int, int> frequency;

    for(int i=0; i<N; i++){
        frequency.insert(arr[i], frequency[arr[i]++]);
    }

    int minElement, maxElement = arr[0];
    int minFreq, maxFreq = frequency[arr[0]];

    for(auto freq: frequency){
        if(freq.second > maxFreq){
            maxFreq = freq.second;
            maxElement = freq.first;
        }

        if(freq.second < minFreq){
            minFreq = freq.second;
            minFreq = freq.first;
        }
    }

    cout << "Highest frequency " << maxElement << " occurs " << maxFreq << " times"; 
    cout << "Lowest frequency " << minElement << " occurs " << minFreq << " times";
    return; 
}

int main(){
    vector<int> arr={10,5,10,15,10,5};
    int N = 5;
    findHighestAnLowestFrequency(arr, N);
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