#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

bool compare(pair<int,int> &a, pair<int, int> &b){
    return a.second < b.second;
}

int main(){
    int t; cin>>t;
    while(t--){
        int n,m; cin>>n>>m;
        vector<int> v;
        while(n--){
            v.push_back(1);
        }
        int count=0;
        vector<pair<int,int>> t;
        for(int i=0; i<m; i++){
            int a,b; cin>>a>>b;
            t.push_back({a,b});
        }
        sort(t.begin(), t.end(), compare);
        for(int i=0; i<m; i++){
            for(int j=(t[i].first-1); j<t[i].second; j++){
                if(v[j]==1){
                    v[j]=0;
                    count++;
                    break;
                }
            }
        }
        cout << count << '\n';
    }
}