#include<bits/stdc++.h>
using namespace std;

void explainSet(){
    set<int> st; // sorted, unique

    st.insert(10); // {10}
    st.emplace(20); // {10,20}
    st.insert(5); // {5,10,20}
    st.insert(10); // {5,10,20}

    for(auto j: st){
        cout << j << endl;
    }

    /* 
    Functionality of insert in vector can be used also,
    that only increases the efficiency

    begin(), end(), rbegin(), rend(), size(),
    empty() and swap are same as those of above
    
    */
    auto it = st.find(20); // return iterator
    cout << *(it) << endl;

    st.erase(5); // {10,20} take logarithimic time

    int cnt = st.count(10);
    cout << "count : " << cnt << endl;

    auto it1 = st.find(10);
    st.erase(it1); // {20} it takes constants time

   //{1,2,3,4,5}
    auto it11 = st.find(2);
    auto it12 = st.find(4);
    st.erase(it11, it12); // after erase {1,4,5} (first, last)

    /*
    lower_bound() and upper_bound() function works in the same way
    as in the vector it does. (learn from attatched video)
    */
   
   /* Syntax*/
   auto lb = st.lower_bound(2);
   auto ub = st.upper_bound(4);

}

int main(){
    explainSet();
    return 0;
}