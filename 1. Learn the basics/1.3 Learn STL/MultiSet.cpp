#include<bits/stdc++.h>
using namespace std;

void explainMultiSet(){
    /* Everything is same as set only stores duplicate elements also */
    /* sorted but not unique */
    multiset<int> ms;
    ms.insert(1); // {1}
    ms.insert(1); // {1,1}
    ms.insert(2); // {1,1,2}
    ms.insert(1); // {1,1,1,2}

    ms.erase(1); // all 1's erased
    int cnt = ms.count(1);
    cout << cnt << endl;

    ms.erase(ms.find(1)); // only a single one erased
    cout << *(ms.find(1)) << endl;
    ms.erase(ms.find(1), (ms.find(1))++); // cannot perform +2 on iterator, a multiset does not store its elements in sequential memory locations like an array or a vector. Instead, a multiset is typically implemented as a balanced binary search tree, such as a red-black tree.
    // The ++ operator on an iterator is overloaded to move the iterator to the next element in the sequence.
    for(auto j: ms){
        cout << j << endl;
    }

    /* rest all functions same as set O(1)*/
}

int main(){
    explainMultiSet();
    return 0;
}