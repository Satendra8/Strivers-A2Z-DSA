#include <bits/stdc++.h>
using namespace std;

void explainVector(){
    vector<int> v; // Dynamic-sized array
    v.push_back(1); // {1}
    v.emplace_back(2); //{1, 2} Faster than push_back

    vector<pair<int, int>> vecp; // Vector of pairs

    vecp.push_back({1,2}); // {{1,2}}
    vecp.emplace_back(3,4); // {{1,2}, {3,4}} Different syntax

    cout << vecp[0].first << " " << vecp[1].second << endl;

    vector<int> vec(5,100); // {100, 100, 100, 100, 100}

    vector<int> vz(5); // {0, 0, 0, 0, 0} Sometimes garbarge depend on compiler

    vector<int> v1(5, 20); // {20, 20, 20, 20, 20}
    vector<int> v2(v1); // copy vector v1 -> v2 {20, 20, 20, 20, 20}
    cout << v1[0] << " " <<v2[1] << endl;

    v.push_back(3);
    v.push_back(4);
    v.push_back(5);

    /* Iterator */
    vector<int>::iterator it = v.begin(); // get the address of immediate left of first element {1, 2, 3, 4, 5}
    cout << *(it) << endl; // 1
    it++;
    cout << *(it) << endl;

    vector<int>::iterator it1 = v.end(); // {1, 2, 3, 4, 5} end will pointer after last location (after 5)
    cout << *(--it1) << endl;

    vector<int> vr;
    vr.push_back(1);
    vr.push_back(2);
    vr.push_back(3);
    vr.push_back(4);
    vr.push_back(5);

    // vector<int>::iterator it2 = vr.rend(); // below is also same.
    auto it2 = vr.rend(); // {5, 4, 3, 2, 1} pointing before 1
    it2 -=2;
    cout << *(it2) << endl; // 2

    // vector<int>::iterator it3 = vr.rbegin();
    auto it3 = vr.rbegin(); //{5, 4, 3, 2, 1} reverse order but access by ++, pointing to 5
    it3 += 2;
    cout << *(it3) << endl; // 3

    /* accessing vector */

    cout << vr[0] << " " << vr.at(1) << endl;

    cout << vr.back() << endl; // access last element

    /* Printing the Vector */

    for(vector<int>::iterator i=vr.begin(); i != vr.end(); i++){
        cout << *(i) << " ";
    }

    //? same but syntax reduced
    for(auto i=vr.begin(); i != vr.end(); i++){ // auto -> automtically detects datatype 
        cout << *(i) << " ";
    }
    cout << endl;
    

    /* For Each Loop */
    for(auto j: v){
        cout << j << " ";
    }
    cout << endl;

    /* Erase */
    v.erase(v.begin());
    v.erase(v.begin()+2, v.begin()+4); // {1, 2, 5} (start, end)

    for(auto j: v){
        cout << j << " ";
    }


    /* Inser function */
    vector<int> vnew(5, 20); //{20, 20, 20, 20, 20}
    vnew.insert(vnew.begin(), 300); // {300, 20, 20, 20, 20, 20}

    vnew.insert(vnew.begin()+1, 2, 400); // {300, 400, 400, 20, 20, 20, 20, 20}

    vector<int> temp(2, 55); // {55, 55}
    vnew.insert(vnew.begin()+5, temp.begin(), temp.end()); // {300, 400, 400, 20, 20, 55, 55, 20, 20, 20}

    cout << vnew.size() << endl; // 10

    vnew.pop_back(); // {300, 400, 400, 20, 20, 55, 55, 20, 20} remove last element

    for(auto j: vnew){
        cout << j << " ";
    }

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
    for(auto j: vnew){
        cout << j << " ";
    }
}

int main(){
    explainVector();
    return 0;
}