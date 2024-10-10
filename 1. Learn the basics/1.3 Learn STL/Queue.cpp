#include<bits/stdc++.h>
using namespace std;


void explainQueue(){
    queue<int> q;

    q.push(10); // {10}
    q.push(20); // {10,20}
    q.emplace(30); // {10,20,30}

    q.back() += 5;
    cout << q.front() << " " << q.back() << endl; // 10 35

    q.pop(); // {20,30}
    cout << q.front() << endl; // 20

    /*
    size, swap, empty, same as stack
    O(1) complexity
    */
}

int main(){
    explainQueue();
    return 0;
}