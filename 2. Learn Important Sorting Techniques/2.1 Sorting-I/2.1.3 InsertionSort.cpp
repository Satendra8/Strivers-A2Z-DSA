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

void insertionSort(int arr[], int N){
    for(int i=1; i<N; i++){
        int index = i;
        for(int j=i-1; j>=0; j--){
            if(arr[index] < arr[j]){
                swap(arr[index], arr[j]);
                index = j;
            }
            else{
                break;
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
    insertionSort(arr, N);
    cout << endl << "Array after Sorting: ";
    for(int i=0; i<N; i++){
        cout << arr[i] << " ";
    }
    return 0;
}


/*
Basic Idea : Iterate over each element and place to it at right position in sorted array (left of that element).
             Inserting each element from an unsorted array to a sorted array.
Complexity : Time => O(N^2), Space => O(N)

Dry Run 1

Input: N = 6, array[] = {13,46,24,52,20,9}

 i         arr
 0     {13,46,24,52,20,9} -> 
 1     {13,46,24,52,20,9} -> j = 0 not swap
 2     {13,24,46,52,20,9} -> j = 1 swap(24,46), j = 0 not swap
 3     {13,24,46,52,20,9} -> j = 2 no swap
 4     {13,20,24,46,52,9} -> j = 3 swap(20,52), j = 2 swap(20,46), j = 1 swap(20,24), j = 0 no swap
 5     {9,13,20,24,46,52} -> j = 4 swap(9,52), j = 3 swap(9,46), j = 2 swap(9,24), j = 1 swap(9,20), j = 0 swap(9,13)
 res   {9,13,20,24,46,52}

*/

/*
Sudo Code

loop over each element from 2 to n

loop from i-1 to 0 and find the right position of element and swap till that element is lesser.

*/