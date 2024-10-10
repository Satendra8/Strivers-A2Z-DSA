#include <bits/stdc++.h>
using namespace std;
/*
Q. Given an array of N integers, write a program to implement the Selection sorting algorithm.

Example 1:
Input: N = 6, array[] = {13,46,24,52,20,9}
Output: 9,13,20,24,46,52
Explanation: After sorting the array is: 9, 13, 20, 24, 46, 52

Example 2:
Input: N=5, array[] = {5,4,3,2,1}
Output: 1,2,3,4,5
Explanation: After sorting the array is: 1, 2, 3, 4, 5

*/

void selectionSort(int arr[], int N){
    for(int i=0; i<N-1; i++){
        int mini = i;
        for(int j=i+1; j<N; j++){
            if(arr[j] < arr[mini]){
                mini = j;
            }
        }
        // cout << "arr[i] " << arr[i] << " mini " << arr[mini] << endl;
        int temp = arr[i];
        arr[i] = arr[mini];
        arr[mini] = temp;
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
    selectionSort(arr, N);
    cout << endl << "Array after Sorting: ";
    for(int i=0; i<N; i++){
        cout << arr[i] << " ";
    }
    return 0;
}


/*
Basic Idea : select smallest and swap
Complexity : Time => O(N^2), Space => O(N)

Dry Run 1

Input: N = 6, array[] = {13,46,24,52,20,9}

 i         arr
 0     {13,46,24,52,20,9} -> j = 5, mini = 5, swap(arr[0], arr[5])
 1     {9,46,24,52,20,13} -> j = 5, mini = 5, swap(arr[1], arr[5])
 2     {9,13,24,52,20,46} -> j = 5, mini = 4, swap(arr[2], arr[4])
 3     {9,13,20,52,24,46} -> j = 5, mini = 4, swap(arr[3], arr[4])
 4     {9,13,20,24,52,46} -> j = 5, mini = 5, swap(arr[4], arr[5])
 res   {9,13,20,24,46,52}

i => (0, N-2)
j => (i+1, N-1)
*/