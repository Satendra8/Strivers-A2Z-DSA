/*
Q. Find Second Smallest and Second Largest Element in an array.

Example 1:
Input: [1,2,4,7,7,5]
Output: Second Smallest : 2
	Second Largest : 5
Explanation: The elements are as follows 1,2,3,5,7,7 and hence second largest of these is 5 and second smallest is 2

Example 2:
Input: [1]
Output: Second Smallest : -1
	Second Largest : -1
Explanation: Since there is only one element in the array, it is the largest and smallest element present in the array. There is no second largest or second smallest element present.

*/
#include <iostream>
using namespace std;



int findSecondLargest(int arr[], int n){
    int largest = INT8_MIN;
    int secondLargest = INT8_MIN;

    // array having single element
    if(n<2){
        return -1;
    }
    for(int i=0; i<n; i++){
        if(arr[i] > largest){
            secondLargest = largest;
            largest = arr[i];
        }
        // ** udpate second largest
        if(arr[i] > secondLargest and arr[i] != largest){
            secondLargest = arr[i];
        }
    }
    return secondLargest;
}


int findSecondSmallest(int arr[], int n){
    int smallest = INT8_MAX;
    int secondSmallest = INT8_MAX;

    // array having single element
    if(n<2){
        return -1;
    }

    for(int i=0; i<n; i++){
        if(arr[i] < smallest){
            secondSmallest = smallest;
            smallest = arr[i];
        }

        if(arr[i] < secondSmallest and arr[i] != smallest){
            secondSmallest = arr[i];
        }
    }
    return secondSmallest;
}

int main(){
    int n;
    cin >> n;
    int arr[n];
    for(int i=0; i<n; i++){
        cin >> arr[i];
    }
    cout << findSecondSmallest(arr, n);
    return 0;
}