#include <iostream>
#include <vector>
#include <numeric>
using namespace std;

int main(){
    int k; cin>>k;
    vector<int> v;
    while(k--){
        int a; cin>>a;
        if(a==0){
            v.pop_back();
        }else{
            v.push_back(a);
        }
    }
    int sum = accumulate(v.begin(), v.end(), 0);
    cout << sum <<'\n';
}
