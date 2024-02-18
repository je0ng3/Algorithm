#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
using namespace std;

int main(){
    int x; cin >> x;
    vector<int> v; v.push_back(64);
    while(true){
        int sum; sum = accumulate(v.begin(), v.end(), 0);
        if(sum==x){
            cout << v.size() <<'\n';
            break;
        }
        int min = *min_element(v.begin(), v.end());
        int min_index = min_element(v.begin(), v.end())-v.begin();
        v[min_index] = min/2;
        sum = accumulate(v.begin(), v.end(), 0);
        if(sum<x){
            v.push_back(min/2);
        }
    }
}