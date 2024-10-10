#include<bits/stdc++.h>
using namespace std;

void explainDeque(){
    deque<int> dq;

    dq.push_back(10); // {10}
    dq.emplace_back(15); // {10, 15}

    dq.push_front(20); // {20, 10, 15}
    dq.emplace_front(5); // {5, 20, 10, 15}

    dq.pop_back(); // {5, 20, 10}
    dq.pop_front(); // {20, 10}

    for(auto j: dq){
        cout << j << " ";
    }

    /*
    rest function same as vector
    begin, end, rbegin, rend, clear, insert, size, swap
    
    */
}


int main(){
    explainDeque();
    return 0;
}