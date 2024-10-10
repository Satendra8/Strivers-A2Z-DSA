#include <bits/stdc++.h>
using namespace std;

void explainPair(){
    pair <int, int> p = {1, 2};
    cout << p.first << " " << p.second;

    pair <int, pair<int, int>> np = {1,{2,4}};
    // cout << np.first << " " << np.second.first << " " << np.second.second;

    pair <int, int> arr[] = {{1,2}, {3,4}, {5,6}, {7,8}};
    cout << arr[3].second <<endl; //6
}

int main(){
    explainPair();
    return 0;
}