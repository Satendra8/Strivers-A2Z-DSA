#include<bits/stdc++.h>
using namespace std;

bool comp(pair<int,int> p1, pair<int,int> p2){
    if(p1.second < p2.second) return true;
    if(p1.second > p2.second) return false;
    if(p1.first > p2.first) return true;
    return false;
}

void explainExtra(){
    int a[5] = {2,1,5,4,6};
    // sort(a, a+4); // ASC order
    sort(a, a+5, greater<int>()); // DESC order
    // sort(v.begin(), v.end()); // for vector
    // sort(a,a+1); // sort only two elements

    pair<int, int> arr[] = {{1,2}, {2,1}, {4,1}};

    // sort it according to second element
    // if second element is same, then sort it according to first element but in descending

    sort(arr, arr+3, comp); // {{4,1}, {2,1}, {1,2}}

    // for(auto i: arr){
    //     cout << i.first << " " << i.second << endl;
    // }

    int num = 7;
    int cnt = __builtin_popcount(num); // count set bits

    long long num1 = 3457688765678;
    int cnt1 = __builtin_popcount(num1); // count set bits
    // cout << cnt1 << endl;

    /* print all permutations */
    string s = "123";
    sort(s.begin(), s.end());

    do{
        cout << s << endl;
    }while(next_permutation(s.begin(), s.end()));
    cout << endl;

    /* find max and min element */
    int arr1[5] = {2,1,5,4,6};
    int maxi = *max_element(a,a+5);
    int mini = *min_element(a,a+5);

    cout << maxi << " " << mini << endl;
}

int main(){
    explainExtra();
    return 0;
}