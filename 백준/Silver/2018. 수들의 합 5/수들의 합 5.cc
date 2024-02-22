#include <iostream>
#include <vector>
#include <numeric>
using namespace std;

int main(){
    int n; cin>>n;
    int count=1;
    vector<int> v;
    for (int i=(n/2)+1; i>=1; i--){
        v.push_back(i);
        int sum = accumulate(v.begin(), v.end(), 0);
        if(sum==n) {
            count++;
            v.erase(v.begin());
        } else if(sum>n) {
            v.erase(v.begin());
        }
    }
    if(n<=2) count--;
    cout << count<<'\n';
}