/*
STL is divided into 4 parts.
Algorithms
Containers
Functions
Iterators
*/
#include <bits/stdc++.h>
using namespace std;

// Pairs
void explainPair(){
    pair <int, int> p = {1, 2};
    // cout << p.first << " " << p.second;
    
    pair <int, pair<int, int>> np = {1,{2,4}};
    // cout << np.first << " " << np.second.first << " " << np.second.second;

    pair <int, int> arr[] = {{1,2}, {3,4}, {5,6}, {7,8}};
    cout << arr[3].second <<endl;
}


// Vector
void explainVector(){
    vector<int> v; // dynamic sized array
    v.push_back(1); // {1}
    v.emplace_back(2); //{1, 2} Faster than push_back

    vector<pair<int, int>> vecp; // vector of pairs

    vecp.push_back({1,2}); // {{1,2}}
    vecp.emplace_back(3,4); // {{1,2}, {3,4}} different syntax

    // cout << vecp[0].first << " " << vecp[1].second << endl;

    vector<int> vec(5,100); // {100, 100, 100, 100, 100}

    vector<int> vz(5); // {0, 0, 0, 0, 0} sometimes garbarge depend on compiler

    vector<int> v1(5, 20); // {20, 20, 20, 20, 20}
    vector<int> v2(v1); // copy vector v1 -> v2 {20, 20, 20, 20, 20}
    // cout << v1[0] << " " <<v2[1] << endl;

    v.push_back(3);
    v.push_back(4);
    v.push_back(5);

    // Iterator
    vector<int>::iterator it = v.begin(); // get the address of immediate left of first element {1, 2, 3, 4, 5}
    //cout << *(it) << endl; // 1
    // it++;
    // cout << *(it) << endl;

    vector<int>::iterator it1 = v.end(); // {1, 2, 3, 4, 5} end will pointer after last location (after 5)
    // cout << *(--it1) << endl;

    vector<int> vr;
    vr.push_back(1);
    vr.push_back(2);
    vr.push_back(3);
    vr.push_back(4);
    vr.push_back(5);

    // vector<int>::iterator it2 = vr.rend(); // below is also same.
    auto it2 = vr.rend(); // {5, 4, 3, 2, 1} pointing before 1
    it2 -=2;
    //cout << *(it2) << endl; // 2

    // vector<int>::iterator it3 = vr.rbegin();
    auto it3 = vr.rbegin(); //{5, 4, 3, 2, 1} reverse order but access by ++, pointing to 5
    it3 += 2;
    // cout << *(it3) << endl; // 3

    /* accessing vector */

    // cout << vr[0] << " " << vr.at(1) << endl;

    // cout << vr.back() << endl; // access last element

    /* Printing the Vector */

    // for(vector<int>::iterator i=vr.begin(); i != vr.end(); i++){
    //     cout << *(i) << " ";
    // }

    // same but syntax reduced
    /*for(auto i=vr.begin(); i != vr.end(); i++){ // auto -> automtically detects datatype 
        cout << *(i) << " ";
    }
    cout << endl;
    */

    /* For Each Loop */
    for(auto j: v){
        cout << j << " ";
    }
    cout << endl;

    /* Erase */
    // v.erase(v.begin());
    v.erase(v.begin()+2, v.begin()+4); // {1, 2, 5} (start, end)

    // for(auto j: v){
    //     cout << j << " ";
    // }


    /* Inser function */
    vector<int> vnew(5, 20); //{20, 20, 20, 20, 20}
    vnew.insert(vnew.begin(), 300); // {300, 20, 20, 20, 20, 20}

    vnew.insert(vnew.begin()+1, 2, 400); // {300, 400, 400, 20, 20, 20, 20, 20}

    vector<int> temp(2, 55); // {55, 55}
    vnew.insert(vnew.begin()+5, temp.begin(), temp.end()); // {300, 400, 400, 20, 20, 55, 55, 20, 20, 20}

    cout << vnew.size() << endl; // 10

    vnew.pop_back(); // {300, 400, 400, 20, 20, 55, 55, 20, 20} remove last element

    // for(auto j: vnew){
    //     cout << j << " ";
    // }

    // t1 -> {10, 20}
    // t2 -> {30, 40}
    vector<int> t1;
    vector<int> t2;

    t1.emplace_back(10);
    t1.emplace_back(20);

    t2.emplace_back(30);
    t2.emplace_back(40);

    t1.swap(t2); // t1 -> {30, 40} t2 -> {10, 20}
    cout << t1[0] << " " << t1[1] << endl; 
    cout << t2[0] << " " << t2[1] << endl;

    vnew.clear(); // erase entire vector
    
    cout << vnew.empty(); // check if vector is empty
    // for(auto j: vnew){
    //     cout << j << " ";
    // }
}


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


void explainSet(){
    set<int> st; // sorted, unique

    st.insert(10); // {10}
    st.emplace(20); // {10,20}
    st.insert(5); // {5,10,20}
    st.insert(10); // {5,10,20}

    // for(auto j: st){
    //     cout << j << endl;
    // }

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


void explainMultiSet(){
    /* Everything is same as set only stores duplicate elements also */
    /* sorted but not unique */
    multiset<int> ms;
    ms.insert(1); // {1}
    ms.insert(1); // {1,1}
    ms.insert(2); // {1,1,2}
    ms.insert(1); // {1,1,1,2}

    // ms.erase(1); // all 1's erased
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

void explainUSet(){
    /* unsorted but unique */

    unordered_set<int> st;
    /*
    lower_bound(), upper_bound() functions does not works rest all functions are same as above,
    it does not store any partucular order it has better complexity than set  in most cases, except when some collision happens.
    
    
    */
    

    /* all oreations are of  O(1)*/
}


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

    // for(auto it: mpp){
    //     cout << it.first << " " << it.second << endl; // traverse a map
    // }
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


void explainMultimap(){
    /*
    everything same as map, only it can store multiple keys
    only mpp[key] cannot be used here
    */

}


void explainUnorderedMap(){
    /* same as set and unordered_set difference */

}


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
    // explainPair();
    // explainVector();
    // explainList();
    // explainDeque();
    // explainStack();
    // explainQueue();
    // explainPQ();
    // explainSet();
    // explainMultiSet();
    // explainUSet();
    // explainMap();
    // explainMultimap();
    // explainUnorderedMap();
    explainExtra();
    return 0;
}