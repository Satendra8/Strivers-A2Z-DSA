#include<bits/stdc++.h>
using namespace std;

void explainStack(){
    stack<int> st;

    st.push(1); // {1}
    st.push(2); // {2,1}
    st.push(3); // {3,2,1}
    st.push(4); // {4,3,2,1}
    st.emplace(5); // {5,4,3,2,1}

    st.pop(); // {4,3,2,1}
    st.pop(); // {3,2,1}
    // cout << st.top() << endl;

    cout << st.size() << endl; // 3
    cout << st.empty() << endl; // 0 check if empty or not

    stack<int> st1, st2;
    st2.push(10);
    st1.swap(st2);

    cout << st1.top() << endl;

    /*
    push, pop, top O(1) complexity
    */
}

int main(){
    explainStack();
    return 0;
}