#include <bits/stdc++.h>
using namespace std;
/*
Q. Given an array of N integers, write a program to implement the Bubble Sorting algorithm.

Example 1:
Input: N = 6, array[] = {13,46,24,52,20,9}
Output: 9,13,20,24,46,52
Explanation: After sorting we get 9,13,20,24,46,52


Input: N = 5, array[] = {5,4,3,2,1}
Output: 1,2,3,4,5
Explanation: After sorting we get 1,2,3,4,5

*/

void bubbleSort(int arr[], int N){
    for(int i=0; i<N-1; i++){
        for(int j=0; j<N-i-1; j++){
            if(arr[j] > arr[j+1]){
                swap(arr[j], arr[j+1]);
            }
        }
    }
    return;
}

int main(){
    int N;
    int arr[N];
    cout << "Enter a Numer ";
    cin >> N;
    for(int i=0; i<N; i++){
        cin >> arr[i];
    }
    bubbleSort(arr, N);
    cout << endl << "Array after Sorting: ";
    for(int i=0; i<N; i++){
        cout << arr[i] << " ";
    }
    return 0;
}


/*
Basic Idea : Large value will go to last (large bubble will go upward)
Complexity : Time => O(N^2), Space => O(N)

Dry Run 1

Input: N = 6, array[] = {13,46,24,52,20,9}


*/

i want to make an animation video on bubble sort using manim

Basic Idea : 
form bubble of numbers (given) Input
make the two comparing bubble with arrow
Swap the bubbles (large bubble will go downward)
Input: N = 6, array[] = {13,46,24,52,20,9}

Code:

void bubbleSort(int arr[], int N){
    for(int i=0; i<N-1; i++){
        for(int j=0; j<N-i-1; j++){
            if(arr[j] > arr[j+1]){
                swap(arr[j], arr[j+1]);
            }
        }
    }
    return;
}