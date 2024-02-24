#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <string>
using namespace std;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n; cin>>n;
    vector<string> v;
    for(int i=0; i<n; i++){
        string s; cin>>s;
        v.push_back(s);
    }
    sort(v.begin(), v.end());
    int count = n;
    for(int i=0; i<n-1; i++){
        if(v[i]==v[i+1].substr(0,v[i].size())){
            count--;
        }    
    }

    cout<<count<<'\n';
    

}