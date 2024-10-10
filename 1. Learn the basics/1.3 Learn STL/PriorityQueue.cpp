#include<bits/stdc++.h>
using namespace std;


void explainPQ(){
    priority_queue<int> pq;

    pq.push(5); // {5}
    pq.push(2); // {5,2}
    pq.push(8); // {8,5,2}
    pq.emplace(10); // {10,8,5,2}

    cout << pq.top() << endl; // 10

    pq.pop(); // {8,5,2}
    cout << pq.top() << endl; // 8

    /* size swap empty function same as others */

    /* Minimum Heap */
    priority_queue<int, vector<int>, greater<int>> pqmin;
    pqmin.push(2); // {2}
    pqmin.push(8); // {2,8}
    pqmin.emplace(6); // {2,6,8}
    pqmin.push(10); // {2,6,8,10}

    cout << pqmin.top() << endl;

    /*
    push, pop, top
    O(1) complexity, O(n) complexity in very worst case
    */
}

int main(){
    explainPQ();
    return 0;
}