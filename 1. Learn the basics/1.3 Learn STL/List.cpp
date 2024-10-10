#include <bits/stdc++.h>
using namespace std;

void explainList(){
    list<int> l1;

    l1.push_back(1); // {1}
    l1.emplace_back(2); // {1, 2}

    l1.push_front(5); // {5, 1, 2}
    l1.emplace_front(10); // {10, 5, 1, 2}
    l1.emplace_front(); // {0, 10, 5, 1, 2}

    for(auto j: l1){
        cout << j << " ";
    }

    /*
    rest function same as vector
    begin, end, rbegin, rend, clear, insert, size, swap
    
    */
}

int main(){
    explainList();
    return 0;
}