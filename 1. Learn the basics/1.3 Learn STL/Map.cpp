#include<bits/stdc++.h>
using namespace std;

void explainMap(){
    /* 
    store data in key value pair
    unique key in sorted order 
    */
    map<int, int> mpp;

    // map<pair<int, int>, int> mp;

    mpp[1] = 10;
    mpp.emplace(2, 20);
    mpp.insert({3, 30}); // it takes in {}

    // {
    //     {1,10},
    //     {2,20},
    //     {3,30},
    // }

    // mp[{2,3}] = 10;

    for(auto it: mpp){
        cout << it.first << " " << it.second << endl; // traverse a map
    }
    cout << mpp[1] << " " << mpp[2] << endl; // access with key
    // cout << mp[{2,3}] << endl;
    cout << mpp[5] << endl; // if not exists then returns 0
    
    auto it1 = mpp.find(2);
    cout << it1->second << endl;

    auto it2 = mpp.find(5); // if element not found then it points to mpp.end(), pointer after last element

    /* This is the syntax */
    auto it3 = mpp.lower_bound(2);
    auto it4 = mpp.upper_bound(3);

    /* erase, swap, size, empty, are same as above */
}

int main(){
    explainMap();
    return 0;
}