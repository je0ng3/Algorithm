#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <string>
using namespace std;

bool compare(string a, string b){
    if(a.size()==b.size()){
        return a<b;
    }
    return a.size()<b.size();
}

int main(){
    int n; cin >> n;
    vector<string> v;
    string s;
    while(n--){
        cin>>s;
        v.push_back(s);
    }
    sort(v.begin(), v.end(), compare);
    v.erase(unique(v.begin(), v.end()), v.end());
    for(int i=0; i<v.size(); i++){
        cout << v[i] << '\n';
    }
}