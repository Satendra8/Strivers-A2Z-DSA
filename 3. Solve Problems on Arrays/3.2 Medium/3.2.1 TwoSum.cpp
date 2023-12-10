/*
Q. Check if a pair with given sum exists in Array.

Example 1:
Input Format: N = 5, arr[] = {2,6,5,8,11}, target = 14
Result: YES (for 1st variant)
       [1, 3] (for 2nd variant)
Explanation: arr[1] + arr[3] = 14. So, the answer is “YES” for the first variant and [1, 3] for 2nd variant.

Example 2:
Input Format: N = 5, arr[] = {2,6,5,8,11}, target = 15
Result: NO (for 1st variant)
	[-1, -1] (for 2nd variant)
Explanation: There exist no such two numbers whose sum is equal to the target.

*/
#include <iostream>
using namespace std;

// N = 5, arr[] = {2,6,5,8,11}, target = 14

bool TwoSumOptimal(int arr[], int target){
    // two pointer

    // l = [2,1,2,4]
    // target = 4

    // l.sort()
    // left = 0
    // right = len(l) - 1

    // while(left<right):
    //     summ = l[left] + l[right]
        
    //     if summ == target:
    //         print("First =>", l[left], "Second =>", l[right])
    //         break
    //     if summ < target:
    //         left += 1
    //     elif summ > target:
    //         right -= 1

    // Complexity
    // Time - O(NlogN)
    // Space - O(1)

    return false;
}

bool TwoSumBest(int arr[], int target){
    // hashing (using set)

    // l = [11,6,5,2,11, 9, 4, 4]
    // target = 8
    // temp = set()


    // for i in l:
    //     diff = target - i
    //     if diff not in temp: # O(1)
    //         temp.add(i)
    //     else:
    //         print("First => ", diff, "Second => ", i)

    // Complexity:
    // Time - O(n)
    // Space - O(n)


    return false;
}

bool TwoSum(int arr[], int target){
    int n = 5;
    for(int i=0; i<n; i++){
        for(int j=i+1; j<n; j++){
            if(arr[i]+arr[j] == target){
                cout << "First, Second " << arr[i] << " " << arr[j];
                return true;
            }
        }
    }
    return false;
}

int main(){
    int n, target;
    cin >> n;
    int arr[n];
    for(int i=0; i<n; i++){
        cin >> arr[i];
    }
    cin >> target;
    TwoSum(arr, target);
    return 0;
}